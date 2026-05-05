from datetime import datetime

now = datetime.now()

new_year_day = datetime(year=now.year, month=1, day=1)
diff = now - new_year_day
days_left = diff.days
print(f"Days left until new year: {days_left}")