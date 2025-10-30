# Multiprocessing is the ability of a program to do multiple things at the same time
# In Python, multiprocessing can be achieved using the multiprocessing module

import multiprocessing

print(multiprocessing.current_process().name) # MainProcess
print(multiprocessing.current_process().ident) # 1234567890
print(multiprocessing.current_process().is_alive()) # True

