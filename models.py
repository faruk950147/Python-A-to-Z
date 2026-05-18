from django.db import models, transaction
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager
)
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError

from datetime import timedelta
import uuid

from account.validators import (
    phone_validator,
    username_validator,
    normalize_phone_number,
    validate_image_size
)

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
# USER MANAGER
# =========================================================
class UserManager(BaseUserManager):

    def create_user(self, username, email, phone, password=None, **extra_fields):

        if not username:
            raise ValueError(_("Username is required"))
        if not email:
            raise ValueError(_("Email is required"))
        if not phone:
            raise ValueError(_("Phone number is required"))

        username = username.strip().lower().replace(" ", "")
        email = self.normalize_email(email).strip().lower()

        phone = normalize_phone_number(phone)
        if not phone:
            raise ValueError(_("Invalid phone number"))

        extra_fields.setdefault("is_active", False)
        extra_fields.setdefault("is_verified", False)

        with transaction.atomic():
            user = self.model(
                username=username,
                email=email,
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

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True"))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True"))

        return self.create_user(username, email, phone, password, **extra_fields)


# =========================================================
# COMMON MIXIN
# =========================================================
class TimeStampMixin(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# =========================================================
# USER MODEL
# =========================================================
class User(AbstractBaseUser, PermissionsMixin, TimeStampMixin):

    # ---------------- BASIC ----------------
    username = models.CharField(
        max_length=150,
        unique=True,
        validators=[username_validator]
    )

    email = models.EmailField(unique=True)
    phone = models.CharField(
        max_length=20,
        unique=True,
        validators=[phone_validator]
    )

    image = models.ImageField(
        upload_to="users/",
        blank=True,
        null=True,
        validators=[
            FileExtensionValidator(["jpg", "jpeg", "png", "webp"]),
            validate_image_size
        ]
    )

    # ---------------- ADDRESS ----------------
    country = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    home_city = models.CharField(max_length=100, null=True, blank=True)
    zip_code = models.CharField(max_length=20, null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    # ---------------- STATUS ----------------
    is_active = models.BooleanField(default=False, db_index=True)
    is_staff = models.BooleanField(default=False, db_index=True)
    is_verified = models.BooleanField(default=False, db_index=True)

    # ---------------- EMAIL VERIFY ----------------
    email_verification_token = models.UUIDField(null=True, blank=True, db_index=True)
    email_token_created_at = models.DateTimeField(null=True, blank=True)

    # ---------------- PASSWORD RESET ----------------
    password_reset_token = models.UUIDField(null=True, blank=True, db_index=True)
    password_reset_token_created_at = models.DateTimeField(null=True, blank=True)

    # ---------------- ONLINE STATUS ----------------
    last_seen = models.DateTimeField(null=True, blank=True, db_index=True)

    # ---------------- SECURITY ----------------
    failed_login_attempts = models.PositiveIntegerField(default=0)
    last_failed_login = models.DateTimeField(null=True, blank=True)
    account_locked_until = models.DateTimeField(null=True, blank=True, db_index=True)

    # ---------------- MANAGER ----------------
    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "phone"]
    EMAIL_FIELD = "email"

    # =====================================================
    # CLEAN
    # =====================================================
    def clean(self):
        super().clean()

        self.username = self.username.strip().lower()
        self.email = self.email.strip().lower()

        phone = normalize_phone_number(self.phone)
        if not phone:
            raise ValidationError({"phone": _("Invalid phone number")})
        self.phone = phone

    # =====================================================
    # SAVE
    # =====================================================
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    # =====================================================
    # ONLINE STATUS
    # =====================================================
    @property
    def is_online(self):
        if not self.last_seen:
            return False
        return timezone.now() <= self.last_seen + timedelta(seconds=ONLINE_TIMEOUT_SECONDS)

    def refresh_last_seen(self):
        now = timezone.now()

        if (
            not self.last_seen or
            (now - self.last_seen).total_seconds() > LAST_SEEN_UPDATE_INTERVAL
        ):
            self.last_seen = now
            self.save(update_fields=["last_seen"])

    # =====================================================
    # ACCOUNT LOCK
    # =====================================================
    @property
    def is_locked(self):
        return bool(
            self.account_locked_until and
            timezone.now() < self.account_locked_until
        )

    # =====================================================
    # FAILED LOGIN
    # =====================================================
    def record_failed_login_attempt(self):
        now = timezone.now()

        with transaction.atomic():
            user = User.objects.select_for_update().get(pk=self.pk)

            user.failed_login_attempts += 1
            user.last_failed_login = now

            if user.failed_login_attempts >= MAX_FAILED_ATTEMPTS:
                user.account_locked_until = now + timedelta(minutes=ACCOUNT_LOCK_MINUTES)

            user.save(update_fields=[
                "failed_login_attempts",
                "last_failed_login",
                "account_locked_until"
            ])

    def reset_login_attempts(self):
        with transaction.atomic():
            user = User.objects.select_for_update().get(pk=self.pk)

            user.failed_login_attempts = 0
            user.last_failed_login = None
            user.account_locked_until = None

            user.save(update_fields=[
                "failed_login_attempts",
                "last_failed_login",
                "account_locked_until"
            ])

    def unlock_account_if_expired(self):
        if self.account_locked_until and timezone.now() >= self.account_locked_until:
            self.account_locked_until = None
            self.failed_login_attempts = 0
            self.save(update_fields=["account_locked_until", "failed_login_attempts"])

    # =====================================================
    # EMAIL VERIFICATION
    # =====================================================
    def generate_email_verification_token(self):
        self.email_verification_token = uuid.uuid4()
        self.email_token_created_at = timezone.now()

        self.save(update_fields=[
            "email_verification_token",
            "email_token_created_at"
        ])

    def email_token_valid(self):
        return (
            self.email_verification_token and
            self.email_token_created_at and
            timezone.now() <= self.email_token_created_at + timedelta(hours=EMAIL_TOKEN_EXPIRE_HOURS)
        )

    def verify_email(self):
        self.is_verified = True
        self.is_active = True
        self.email_verification_token = None
        self.email_token_created_at = None

        self.save(update_fields=[
            "is_verified",
            "is_active",
            "email_verification_token",
            "email_token_created_at"
        ])

    # =====================================================
    # PASSWORD RESET
    # =====================================================
    def generate_password_reset_token(self):
        self.password_reset_token = uuid.uuid4()
        self.password_reset_token_created_at = timezone.now()

        self.save(update_fields=[
            "password_reset_token",
            "password_reset_token_created_at"
        ])

    def password_reset_valid(self):
        return (
            self.password_reset_token and
            self.password_reset_token_created_at and
            timezone.now() <= self.password_reset_token_created_at + timedelta(hours=RESET_TOKEN_EXPIRE_HOURS)
        )

    def clear_password_reset_token(self):
        self.password_reset_token = None
        self.password_reset_token_created_at = None

        self.save(update_fields=[
            "password_reset_token",
            "password_reset_token_created_at"
        ])

    # =====================================================
    # DISPLAY
    # =====================================================
    def get_last_seen_display(self):
        if self.is_online:
            return _("Online")
        if not self.last_seen:
            return _("Never")
        return timezone.localtime(self.last_seen).strftime("%Y-%m-%d %H:%M")

    def __str__(self):
        return self.username or self.email

    class Meta:
        db_table = "account_users"
        verbose_name = "User"
        verbose_name_plural = "Users"

        ordering = ["-id"]

        indexes = [
            models.Index(fields=["email_verification_token"]),
            models.Index(fields=["password_reset_token"]),
            models.Index(fields=["is_active", "is_verified"]),
            models.Index(fields=["created_at"]),
            models.Index(fields=["last_seen"]),
        ]