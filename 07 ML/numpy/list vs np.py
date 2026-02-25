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
import sys
# ======================== sum of list python way ========================
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

# start = time.time()
# total = sum(data)
# end = time.time()
# print("Python sum:", total)
# print("Python sum time:", end - start, "seconds")

# ======================== sum of list numpy way ========================
# arr = np.array(data)
# start = time.time()
# total = np.sum(arr)
# end = time.time()
# print("NumPy sum:", total)
# print("NumPy sum time:", end - start, "seconds")

# start = time.time()
# total = np.sum(data)
# end = time.time()
# print("NumPy sum:", total)
# print("NumPy sum time:", end - start, "seconds")


# ======================== sum of list numpy way ========================
start_time = time.time()
print(f"Time taken to create list with 10 million elements: {start_time}")
lst = [1,2,3,4,5,6,7,8,9,10] * 1000000
print("List length:", len(lst))
print("List memory usage:", sys.getsizeof(lst), "bytes")
end_time = time.time()
print(f"Time taken to create list: {end_time - start_time} seconds")

# ======================== sum of list numpy way ========================
start_time = time.time()
print(f"Time taken to create numpy array with 10 million elements: {start_time}")
arr = np.array([1,2,3,4,5,6,7,8,9,10] * 1000000)
print("Array length:", len(arr))
print("Array memory usage:", arr.nbytes, "bytes")
end_time = time.time()
print(f"Time taken to create numpy array: {end_time - start_time} seconds")

