from datetime import datetime

ONLINE_TIMEOUT_SECONDS = 60  # 60 seconds
EMAIL_TOKEN_EXPIRE_SECONDS = 60 * 60 * 24  # 24 hours
RESET_TOKEN_EXPIRE_SECONDS = 60 * 60 * 2  # 2 hours
ACCOUNT_LOCK_MINUTES = 15  # 15 minutes
MAX_FAILED_ATTEMPTS = 5  # 5 attempts
ATTEMPT_TIMEOUT = 60 * 60  # 1 hour

now = datetime.now()

# total_seconds = now.timestamp()
total_seconds = (now.hour * 3600 + now.minute * 60 + now.second)
minutes = total_seconds // 60
hours = minutes // 60
days = hours // 24
print(f"Total seconds: {int(total_seconds)}")
print(f"Total minutes: {int(minutes)}")
print(f"Total hours: {int(hours)}")
print(f"Total days: {int(days)}")