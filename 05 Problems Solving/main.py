from datetime import datetime

ONLINE_TIMEOUT_SECONDS = 60
EMAIL_TOKEN_EXPIRE_SECONDS = 60 * 60 * 24
RESET_TOKEN_EXPIRE_SECONDS = 60 * 60 * 2
ACCOUNT_LOCK_MINUTES = 15
MAX_FAILED_ATTEMPTS = 5
ATTEMPT_TIMEOUT = 60 * 60

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