"""
Numpy is a library for the Python programming language, 
adding support for large, multi-dimensional arrays and matrices, 
along with a large collection of high-level mathematical functions to operate on these arrays.
"""
import time
import numpy as np

N = 10000000  # 10 million data points

"""
# Pure Python implementation
start_time = time.time()
print("Pure Python implementation")
python_array = range(N)
python_sum = 0
for i in python_array:
    python_sum += i
print("Python sum:", python_sum)
print(f"Python time: {time.time() - start_time:.4f} seconds\n")
"""


# NumPy implementation
start_time = time.time()
print("NumPy implementation")
numpy_array = np.arange(N)
numpy_sum = np.sum(numpy_array)
print("NumPy sum:", numpy_sum)
print(f"NumPy time: {time.time() - start_time:.4f} seconds")

