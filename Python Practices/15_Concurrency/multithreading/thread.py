# Multithreading is the ability of a program to do multiple things at the same time
# In Python, multithreading can be achieved using the threading module

import threading

print(threading.current_thread()) # <_MainThread(MainThread, started 1234567890)>
print(threading.current_thread().name) # MainThread
print(threading.current_thread().ident) # 1234567890
print(threading.current_thread().is_alive()) # True
