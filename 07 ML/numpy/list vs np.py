"""
list vs np.array
list is dynamic
np.array is static

list is slow
np.array is fast

list is not homogenous
np.array is homogenous

list is not fixed size
np.array is fixed size

list is not memory efficient
np.array is memory efficient

list is not thread safe
np.array is thread safe

list is not safe
np.array is safe

"""
import time
import numpy as np

# 10 million data create 
data = range(10000000)

# Python loop
# start = time.time()
# total = 0
# for x in data:
#     total += x
# end = time.time()
# print("Python loop sum:", total)
# print("Python loop time:", end - start, "seconds")

start = time.time()
total = sum(data)
end = time.time()
print("Python sum:", total)
print("Python sum time:", end - start, "seconds")

# NumPy sum
# arr = np.array(data)
# start = time.time()
# total = np.sum(arr)
# end = time.time()
# print("NumPy sum:", total)
# print("NumPy sum time:", end - start, "seconds")

start = time.time()
total = np.sum(data)
end = time.time()
print("NumPy sum:", total)
print("NumPy sum time:", end - start, "seconds")