import datetime

""" # Get today's date
today = datetime.date.today()
print(today)

# Get the current time
now = datetime.datetime.now()
print(now)

# Get the current time in a specific format
now = datetime.datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))

# Get the current time in a specific format
now = datetime.datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))
 """
 
date = datetime.datetime.now()
print(date.day)
print(date.month)
print(date.year)