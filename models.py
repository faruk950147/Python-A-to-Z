from django.db import models, transaction
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.utils.timezone import localtime
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager
)
from django.contrib import admin
from django.utils.html import format_html

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

        normalized_phone = normalize_phone_number(phone)
        if not normalized_phone:
            raise ValueError(_("Invalid phone number"))

        # Optional: restrict extra fields
        allowed_fields = {
            "is_active",
            "is_verified",
        }

        for key in extra_fields:
            if key not in allowed_fields:
                raise ValueError(_("Invalid field: %s") % key)

        with transaction.atomic():

            user = self.model(
                username=username,
                email=email,
                phone=normalized_phone,
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

        return self.create_user(
            username=username,
            email=email,
            phone=phone,
            password=password,
            **extra_fields
        )

# =========================================================
# COMMON MIXIN
# =========================================================
class CommonMixins(models.Model):

    created_at = models.DateTimeField(_("created_at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated_at"), auto_now=True)

    @property
    def image_tag(self):
        image = getattr(self, "image", None)

        if image and hasattr(image, "url"):
            return format_html(
                '<img src="{}" width="50" height="50" style="border-radius:5px;" />',
                image.url
            )

        return format_html("<span>No Image</span>")

    class Meta:
        abstract = True


# =========================================================
# USER MODEL
# =========================================================
class User(AbstractBaseUser, PermissionsMixin, CommonMixins):
    
    # =====================================================
    # BASIC
    # =====================================================
    username = models.CharField(
        _("username"), max_length=150, unique=True, validators=[username_validator]
    )
    email = models.EmailField(
        _("email"), max_length=255, unique=True
    )
    phone = models.CharField(
        _("phone"), max_length=15, unique=True, validators=[phone_validator]
    )

    image = models.ImageField(
        _("image"), upload_to="users/", blank=True, null=True,
        validators=[
            FileExtensionValidator(allowed_extensions=["jpg", "jpeg", "png", "webp"]),
            validate_image_size
        ]
    )

    # =====================================================
    # ADDRESS
    # =====================================================
    country = models.CharField(_("country"), max_length=100, null=True, blank=True)
    city = models.CharField(_("city"), max_length=100, null=True, blank=True)
    home_city = models.CharField(_("home_city"), max_length=100, null=True, blank=True)
    zip_code = models.CharField(_("zip_code"), max_length=20, null=True, blank=True)

    address = models.TextField(_("address"), null=True, blank=True)

    # =====================================================
    # STATUS
    # =====================================================
    is_active = models.BooleanField(_("is_active"), default=False, db_index=True)
    is_staff = models.BooleanField(_("is_staff"), default=False, db_index=True)
    is_verified = models.BooleanField(_("is_verified"), default=False, db_index=True)
    

    # =====================================================
    # EMAIL VERIFICATION
    # =====================================================
    email_verification_token = models.UUIDField(
        _("email_verification_token"), null=True, blank=True, db_index=True
    )

    email_token_created_at = models.DateTimeField(
        _("email_token_created_at"),
        null=True,
        blank=True
    )

    # =====================================================
    # PASSWORD RESET
    # =====================================================
    password_reset_token = models.UUIDField(
        _("password_reset_token"), null=True, blank=True, db_index=True
    )

    password_reset_token_created_at = models.DateTimeField(
        _("password_reset_token_created_at"), null=True, blank=True
    )

    # =====================================================
    # ONLINE STATUS
    # =====================================================
    last_seen = models.DateTimeField(
        _("last_seen"), null=True, blank=True, db_index=True
    )

    # =====================================================
    # SECURITY
    # =====================================================
    failed_login_attempts = models.PositiveIntegerField(
        _("failed_login_attempts"),
        default=0
    )

    last_failed_login = models.DateTimeField(
        _("last_failed_login"), null=True, blank=True
    )

    account_locked_until = models.DateTimeField(
        _("account_locked_until"), null=True, blank=True, db_index=True
    )

    # =====================================================
    # MANAGER
    # =====================================================
    objects = UserManager()

    USERNAME_FIELD = "username"

    REQUIRED_FIELDS = ["email", "phone"]

    # =====================================================
    # CLEAN
    # =====================================================
    def clean(self):

        super().clean()

        if self.username:
            self.username = self.username.strip().lower()

        if self.email:
            self.email = self.email.strip().lower()

        if self.phone:
            normalized_phone = normalize_phone_number(self.phone)
            if not normalized_phone:
                raise ValidationError({"phone": _("Invalid phone number")})
            self.phone = normalized_phone

    # =====================================================
    # SAVE
    # =====================================================
    def save(self, *args, **kwargs):

        validate = kwargs.pop("validate", True)

        if validate:
            self.full_clean()

        super().save(*args, **kwargs)

    # =====================================================
    # ONLINE STATUS
    # =====================================================
    @property
    def is_online(self):
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