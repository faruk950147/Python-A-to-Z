from django.db import models, transaction
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.utils.timezone import localtime
from django.core.validators import RegexValidator, FileExtensionValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager
)
from django.utils.html import format_html

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
# VALIDATORS
# =========================================================
phone_validator = RegexValidator(
    r"^\+?\d{10,15}$",
    "Enter a valid phone number"
)

username_validator = RegexValidator(
    regex=r"^[a-zA-Z0-9_]+$",
    message="Username can contain only letters, numbers and underscore"
)

# =========================================================
# PHONE NORMALIZER
# =========================================================
def normalize_phone_number(phone):
    if not phone:
        return None
    phone = re.sub(r"\s+", "", phone)
    if phone.startswith("+880"):
        return phone
    if phone.startswith("880"):
        return "+" + phone
    if phone.startswith("01"):
        return "+880" + phone[1:]
    return phone


# =========================================================
# USER MANAGER
# =========================================================
class UserManager(BaseUserManager):

    def create_user(self, username, email, phone, password=None, **extra_fields):

        if not username or not email or not phone:
            raise ValueError("Username, Email and Phone are required")

        phone = normalize_phone_number(phone)
        if not phone:
            raise ValueError("Invalid Bangladeshi phone number")

        user = self.model(
            username=username.strip().lower(),
            email=self.normalize_email(email).strip().lower(),
            phone=phone,
            **extra_fields
        )

        user.set_password(password) if password else user.set_unusable_password()
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
    '''Custom User model with extended fields and functionality
    
    - Unique username, email and phone fields
    why using translation 
    translation is used to make the field names translatable in case 
    we want to support multiple languages in the future. 
    It allows us to provide localized field names in forms and admin interface without 
    changing the code.
    '''

    # BASIC
    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        validators=[username_validator]
    )

    email = models.EmailField(
        _("email"),
        max_length=255,
        unique=True
    )

    phone = models.CharField(
        _("phone"),
        max_length=14,
        unique=True,
        validators=[phone_validator]
    )

    image = models.ImageField(
        _("image"),
        upload_to="users/",
        blank=True,
        null=True,
        validators=[FileExtensionValidator(["jpg", "jpeg", "png", "webp"])]
    )

    # ADDRESS
    country = models.CharField(_("country"), max_length=100, blank=True, null=True)
    city = models.CharField(_("city"), max_length=100, blank=True, null=True)
    home_city = models.CharField(_("home_city"), max_length=100, blank=True, null=True)
    zip_code = models.CharField(_("zip_code"), max_length=20, blank=True, null=True)
    address = models.TextField(_("address"), blank=True, null=True)

    # STATUS
    is_active = models.BooleanField(_("is_active"), default=False, db_index=True)
    is_staff = models.BooleanField(_("is_staff"), default=False, db_index=True)
    is_verified = models.BooleanField(_("is_verified"), default=False, db_index=True)

    # TOKENS
    email_verification_token = models.UUIDField(_("email_verification_token"), null=True, blank=True, db_index=True)
    email_token_created_at = models.DateTimeField(_("email_token_created_at"), null=True, blank=True)

    password_reset_token = models.UUIDField(_("password_reset_token"), null=True, blank=True, db_index=True)
    password_reset_token_created_at = models.DateTimeField(_("password_reset_token_created_at"), null=True, blank=True)

    # ONLINE
    last_seen = models.DateTimeField(_("last_seen"), null=True, blank=True, db_index=True)

    # SECURITY
    failed_login_attempts = models.PositiveIntegerField(_("failed_login_attempts"), default=0)
    last_failed_login = models.DateTimeField(_("last_failed_login"), null=True, blank=True)
    account_locked_until = models.DateTimeField(_("account_locked_until"), null=True, blank=True, db_index=True)

    # TIMESTAMPS
    created_at = models.DateTimeField(_("created_at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated_at"), auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "phone"]

    # =====================================================
    # CLEAN (validation only)
    # =====================================================
    def clean(self):
        super().clean()

        if self.phone:
            if not normalize_phone_number(self.phone):
                raise ValidationError({"phone": "Invalid phone number"})

    # =====================================================
    # SAVE (normalization only)
    # =====================================================
    def save(self, *args, **kwargs):
        if self.username:
            self.username = self.username.strip().lower()

        if self.email:
            self.email = self.email.strip().lower()

        if self.phone:
            self.phone = normalize_phone_number(self.phone)

        super().save(*args, **kwargs)

    # =====================================================
    # ONLINE STATUS
    # =====================================================
    @property
    def is_online(self):
        if not self.last_seen:
            return False
        
        return bool(
            self.last_seen and
            timezone.now() <= self.last_seen + timedelta(seconds=ONLINE_TIMEOUT_SECONDS)
        )

    def refresh_last_seen(self):
        now = timezone.now()

        if not self.last_seen or (now - self.last_seen).total_seconds() > LAST_SEEN_UPDATE_INTERVAL:
            self.last_seen = now
            self.save(update_fields=["last_seen"])

    # =====================================================
    # ACCOUNT LOCK
    # =====================================================
    @property
    def is_locked(self):
        return bool(self.account_locked_until and 
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
            self.save(update_fields=[
                "account_locked_until",
                "failed_login_attempts"
            ])

    # =====================================================
    # EMAIL TOKEN
    # =====================================================
    def generate_email_verification_token(self):
        self.email_verification_token = uuid.uuid4()
        self.email_token_created_at = timezone.now()

        self.save(update_fields=["email_verification_token", "email_token_created_at"])

    def has_valid_email_verification_token(self):
        return (
            self.email_verification_token and
            self.email_token_created_at and
            timezone.now() <= self.email_token_created_at + timedelta(hours=EMAIL_TOKEN_EXPIRE_HOURS)
        )

    def mark_email_as_verified(self):
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

    def has_valid_password_reset_token(self):
        return (
            self.password_reset_token and
            self.password_reset_token_created_at and
            timezone.now() <= self.password_reset_token_created_at + timedelta(hours=RESET_TOKEN_EXPIRE_HOURS)
        )

    def remove_password_reset_token(self):
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
        return localtime(self.last_seen).strftime("%Y-%m-%d %H:%M")

    @property
    def image_tag(self):
        img = getattr(self, 'image', None)
        if img and hasattr(img, 'url'):
            return format_html('<img src="{}" style="max-width:50px; max-height:50px;" />', img.url)
        return format_html('<span>No Image</span>')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = _("01. Users")
        db_table = "account_users"
        ordering = ["-id"]

        indexes = [
            models.Index(fields=["email_verification_token"]),
            models.Index(fields=["password_reset_token"]),
            models.Index(fields=["is_active", "is_verified"]),
            models.Index(fields=["created_at"]),
            models.Index(fields=["last_seen"]),
        ]