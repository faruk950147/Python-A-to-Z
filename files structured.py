"""
account/
│
├── models.py
├── managers.py
├── services/
│   ├── auth_service.py
│   ├── token_service.py
│   ├── user_service.py
│
├── utils/
│   ├── validators.py
│   ├── helpers.py
│
├── middleware/
│   ├── last_seen_middleware.py
│   ├── online_status_middleware.py
│
├── api/
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│
└── constants.py

2. constants.py
class AccountConfig:
    ONLINE_TIMEOUT_SECONDS = 60
    LAST_SEEN_UPDATE_INTERVAL = 30

    ACCOUNT_LOCK_MINUTES = 15
    MAX_FAILED_ATTEMPTS = 5

    EMAIL_TOKEN_EXPIRE_HOURS = 24
    RESET_TOKEN_EXPIRE_HOURS = 1

3. SERVICE LAYER (MOST IMPORTANT)
auth_service.py
from django.utils import timezone
from django.contrib.auth import authenticate

from account.models import User


class AuthService:

    @staticmethod
    def login_user(username, password):

        user = authenticate(username=username, password=password)

        if not user:
            return None, "Invalid credentials"

        if user.is_locked:
            return None, "Account locked"

        user.reset_failed_logins()

        return user, None
token_service.py
import uuid
from django.utils import timezone


class TokenService:

    @staticmethod
    def generate_email_token(user):

        user.email_verification_token = uuid.uuid4()
        user.email_verification_sent_at = timezone.now()
        user.save(update_fields=[
            "email_verification_token",
            "email_verification_sent_at",
        ])

    @staticmethod
    def generate_reset_token(user):

        user.password_reset_token = uuid.uuid4()
        user.password_reset_requested_at = timezone.now()

        user.save(update_fields=[
            "password_reset_token",
            "password_reset_requested_at",
        ])
user_service.py
from django.utils import timezone


class UserService:

    @staticmethod
    def update_last_seen(user):

        now = timezone.now()

        user.last_seen_at = now
        user.save(update_fields=["last_seen_at"])
4. MIDDLEWARE (AUTO ONLINE SYSTEM)
last_seen_middleware.py
from django.utils import timezone


class LastSeenMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        response = self.get_response(request)

        user = getattr(request, "user", None)

        if user and user.is_authenticated:

            now = timezone.now()

            if (
                not user.last_seen_at or
                (now - user.last_seen_at).total_seconds() >= 30
            ):
                user.last_seen_at = now
                user.save(update_fields=["last_seen_at"])

        return response
5. SECURITY LAYER IMPROVEMENT
Login protection (recommended)

Add decorator/service:

def check_account_lock(user):

    if user.is_locked:
        raise Exception("Account is locked")
6. CLEAN MODEL (FINAL OPTIMIZED VERSION IDEA)

Model should ONLY contain:

fields
small helpers
no heavy business logic
RULE:
Layer	Responsibility
Model	Data only
Service	Business logic
Middleware	Auto updates
API	Request handling
7. PERFORMANCE IMPROVEMENTS
Add DB indexes
indexes = [
    models.Index(fields=["email"]),
    models.Index(fields=["phone"]),
    models.Index(fields=["username"]),
    models.Index(fields=["is_active", "is_email_verified"]),
    models.Index(fields=["last_seen_at"]),
    models.Index(fields=["account_locked_until"]),
]
✔ Use only required fields
User.objects.only("id", "username", "email", "last_seen_at")
8. SECURITY BEST PRACTICES
✔ Must enable:
AUTH_PASSWORD_VALIDATORS = True
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
✔ Prevent brute force
failed login tracking ✔
account lock ✔
optional: IP tracking middleware
9. FINAL SYSTEM FLOW
LOGIN FLOW:
User enters credentials
        ↓
AuthService.login_user()
        ↓
check is_locked
        ↓
authenticate()
        ↓
reset_failed_logins()
        ↓
return user
REGISTER FLOW:
create_user()
        ↓
TokenService.generate_email_token()
        ↓
send email verification
ONLINE STATUS FLOW:
request comes
        ↓
LastSeenMiddleware runs
        ↓
update last_seen_at


"""