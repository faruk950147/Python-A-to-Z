from django.db import models, transaction
from django.utils import timezone
from django.utils.timezone import localtime
from django.core.validators import RegexValidator
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager
)
from django.db.models.functions import Lower

from datetime import timedelta
import uuid
import re


# =========================================================
# CONFIG
# =========================================================
ONLINE_TIMEOUT_SECONDS = 60
LAST_SEEN_UPDATE_INTERVAL = 30

ACCOUNT_LOCK_MINUTES = 15
MAX_FAILED_ATTEMPTS = 5

EMAIL_TOKEN_EXPIRE_HOURS = 24
RESET_TOKEN_EXPIRE_HOURS = 1


# =========================================================
# PHONE NORMALIZER
# =========================================================
def normalize_bangladeshi_phone_number(phone):
    if not phone:
        return None

    phone = str(phone).strip()
    phone = re.sub(r"\D", "", phone)

    # 01XXXXXXXXX → +8801XXXXXXXXX
    if phone.startswith("01") and len(phone) == 11:
        return "+880" + phone[1:]

    # 8801XXXXXXXXX → +8801XXXXXXXXX
    if phone.startswith("880") and len(phone) == 13:
        return "+" + phone

    # already correct format
    if phone.startswith("+8801"):
        return phone

    return None


# =========================================================
# VALIDATORS
# =========================================================
phone_validator = RegexValidator(
    regex=r"^(?:\+8801|01)[3-9]\d{8}$",
    message="Enter a valid Bangladeshi phone number"
)

username_validator = RegexValidator(
    regex=r"^[a-zA-Z0-9_]+$",
    message="Username can contain only letters, numbers and underscore"
)


# =========================================================
# USER MANAGER
# =========================================================
class UserManager(BaseUserManager):

    def create_user(self, username, email, phone, password=None, **extra_fields):

        if not username:
            raise ValueError("Username is required")
        if not email:
            raise ValueError("Email is required")
        if not phone:
            raise ValueError("Phone is required")

        phone = normalize_bangladeshi_phone_number(phone)

        user = self.model(
            username=username.strip().lower(),
            email=self.normalize_email(email).strip().lower(),
            phone=phone,
            **extra_fields
        )

        if password:
            user.set_password(password)
        else:
            user.set_unusable_password()

        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, phone, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_verified", True)

        return self.create_user(username, email, phone, password, **extra_fields)


# =========================================================
# USER MODEL
# =========================================================
class User(AbstractBaseUser, PermissionsMixin):

    # ---------------- BASIC ----------------
    username = models.CharField(
        max_length=150,
        unique=True,
        db_index=True,
        validators=[username_validator]
    )

    email = models.EmailField(unique=True, db_index=True)

    phone = models.CharField(
        max_length=14,
        unique=True,
        db_index=True,
        validators=[phone_validator]
    )

    image = models.ImageField(upload_to="users/", blank=True, null=True)

    # ---------------- ADDRESS ----------------
    country = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    home_city = models.CharField(max_length=100, blank=True, null=True)
    zip_code = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    # ---------------- STATUS ----------------
    is_active = models.BooleanField(default=False, db_index=True)
    is_staff = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False, db_index=True)

    # ---------------- EMAIL TOKEN ----------------
    email_verification_token = models.UUIDField(blank=True, null=True, db_index=True)
    email_token_created_at = models.DateTimeField(blank=True, null=True)

    # ---------------- PASSWORD RESET ----------------
    password_reset_token = models.UUIDField(blank=True, null=True, db_index=True)
    password_reset_token_created_at = models.DateTimeField(blank=True, null=True)

    # ---------------- ONLINE ----------------
    last_seen = models.DateTimeField(blank=True, null=True, db_index=True)

    # ---------------- SECURITY ----------------
    failed_login_attempts = models.PositiveIntegerField(default=0)
    last_failed_login = models.DateTimeField(blank=True, null=True)
    account_locked_until = models.DateTimeField(blank=True, null=True, db_index=True)

    # ---------------- TIMESTAMPS ----------------
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "phone"]

    # =====================================================
    # CLEAN
    # =====================================================
    def clean(self):
        if self.username:
            self.username = self.username.strip().lower()

        if self.email:
            self.email = self.email.strip().lower()

        if self.phone:
            self.phone = normalize_bangladeshi_phone_number(self.phone)

    # =====================================================
    # SAVE (SAFE)
    # =====================================================
    def save(self, *args, **kwargs):
        if self.phone:
            normalized = normalize_bangladeshi_phone_number(self.phone)

            if not normalized:
                raise ValueError("Invalid Bangladeshi phone number")

            self.phone = normalized

        super().save(*args, **kwargs)

    # =====================================================
    # ONLINE STATUS
    # =====================================================
    @property
    def is_online(self):
        if not self.last_seen:
            return False

        return (timezone.now() - self.last_seen).total_seconds() < ONLINE_TIMEOUT_SECONDS

    def refresh_last_seen(self):
        now = timezone.now()

        if not self.last_seen or (now - self.last_seen).total_seconds() > LAST_SEEN_UPDATE_INTERVAL:
            User.objects.filter(pk=self.pk).update(last_seen=now)
            self.last_seen = now

    # =====================================================
    # ACCOUNT LOCK
    # =====================================================
    @property
    def is_locked(self):
        return bool(self.account_locked_until and timezone.now() < self.account_locked_until)

    # =====================================================
    # LOGIN SECURITY
    # =====================================================
    def record_failed_login_attempt(self):
        now = timezone.now()

        with transaction.atomic():
            user = User.objects.select_for_update().get(pk=self.pk)

            user.failed_login_attempts += 1
            user.last_failed_login = now

            if user.failed_login_attempts >= MAX_FAILED_ATTEMPTS:
                user.account_locked_until = now + timedelta(minutes=ACCOUNT_LOCK_MINUTES)

            user.save()

    def reset_login_attempts(self):
        with transaction.atomic():
            user = User.objects.select_for_update().get(pk=self.pk)

            user.failed_login_attempts = 0
            user.last_failed_login = None
            user.account_locked_until = None

            user.save()

    # =====================================================
    # EMAIL VERIFICATION
    # =====================================================
    def generate_email_verification_token(self):
        self.email_verification_token = uuid.uuid4()
        self.email_token_created_at = timezone.now()

    def has_valid_email_verification_token(self):
        if not self.email_verification_token:
            return False
        if not self.email_token_created_at:
            return False

        return timezone.now() <= self.email_token_created_at + timedelta(hours=EMAIL_TOKEN_EXPIRE_HOURS)

    def mark_email_as_verified(self):
        self.is_verified = True
        self.is_active = True
        self.email_verification_token = None
        self.email_token_created_at = None

    # =====================================================
    # PASSWORD RESET
    # =====================================================
    def generate_password_reset_token(self):
        self.password_reset_token = uuid.uuid4()
        self.password_reset_token_created_at = timezone.now()

    def has_valid_password_reset_token(self):
        if not self.password_reset_token:
            return False
        if not self.password_reset_token_created_at:
            return False

        return timezone.now() <= self.password_reset_token_created_at + timedelta(hours=RESET_TOKEN_EXPIRE_HOURS)

    def remove_password_reset_token(self):
        self.password_reset_token = None
        self.password_reset_token_created_at = None

    # =====================================================
    # DISPLAY
    # =====================================================
    def get_last_seen_display(self):
        if self.is_online:
            return "Online"
        if not self.last_seen:
            return "Never"
        return localtime(self.last_seen).strftime("%Y-%m-%d %H:%M")

    def __str__(self):
        return f"{self.username} ({self.email})"

    # =====================================================
    # META
    # =====================================================
    class Meta:
        db_table = "account_users"
        ordering = ["-id"]

        constraints = [
            models.CheckConstraint(check=~models.Q(username=""), name="username_not_empty"),
            models.CheckConstraint(check=~models.Q(email=""), name="email_not_empty"),
            models.CheckConstraint(check=~models.Q(phone=""), name="phone_not_empty"),
            models.UniqueConstraint(Lower("email"), name="unique_lower_email"),
            models.UniqueConstraint(Lower("username"), name="unique_lower_username"),
        ]