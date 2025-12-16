import datetime

# current date and time
current_date_time = datetime.datetime.now()
print(current_date_time)

# current date
current_date = datetime.date.today()
print(current_date)

# current time (FIXED)
current_time = datetime.datetime.now().time()
print(current_time)

# current year
current_year = datetime.datetime.now()
print(current_year.year)

# current month
current_month = datetime.datetime.now()
print(current_month.month)

# current day
current_day = datetime.datetime.now()
print(current_day.day)

# format string
formatted_date_time = datetime.datetime.now()
print(formatted_date_time.strftime("%Y-%m-%d %H:%M:%S"))
