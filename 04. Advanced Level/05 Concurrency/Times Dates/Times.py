import time
# ========================= time() ==============================
timestamp = time.time() # Returns the current time in seconds since the epoch
print(timestamp)
# output: 1746166522.1234567

# ========================= sleep() ==============================
time.sleep(5) # Suspends (delays) execution for the given number of seconds
print("5 seconds have passed")
# output: 5 seconds have passed

# ========================= ctime() ==============================
time.ctime(timestamp) # Converts a time in seconds since the epoch to a readable string
print(time.ctime(timestamp))
# output: Wed Jan  1 00:00:00 2025


# ========================= perf_counter() ==============================
time.perf_counter() # Returns the current value of the performance counter, a clock with the highest available resolution to measure a short duration
print(time.perf_counter())
# output: 1746166522.1234567

# ========================= process_time() ==============================
time.process_time() # Returns the current value of the process time, a clock that is not affected by sleep or other system activity
print(time.process_time())
# output: 1746166522.1234567

# ========================= monotonic() ==============================
time.monotonic() # Returns the current value of the monotonic clock, a clock that cannot go backwards
print(time.monotonic())
# output: 1746166522.1234567

# ========================= local() ==============================
time.localtime() # Returns the current local time as a struct_time object
print(time.localtime())
# output: time.struct_time(tm_year=2025, tm_mon=1, tm_mday=1, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=1, tm_isdst=0)

# ========================= gmtime() ==============================
time.gmtime() # Returns the current UTC time as a struct_time object
print(time.gmtime())
# output: time.struct_time(tm_year=2025, tm_mon=1, tm_mday=1, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=1, tm_isdst=0)

# ========================= struct_time() ==============================
time.struct_time() # Returns a struct_time object from a time in seconds since the epoch
print(time.struct_time())
# output: time.struct_time(tm_year=2025, tm_mon=1, tm_mday=1, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=1, tm_isdst=0)

# ========================= strptime() ==============================
time.strptime() # Returns a struct_time object from a time in seconds since the epoch
print(time.strptime())
# output: time.struct_time(tm_year=2025, tm_mon=1, tm_mday=1, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=1, tm_isdst=0)
