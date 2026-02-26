import numpy as np
"""
order: 'C' (row-major), 'F' (column-major), 'A' (Fortran if memory-contiguous, else C), 'K' (as stored)
axis: 0 (down rows), 1 (across columns)

"""

# Create a 1D array
arr = np.array([1, 2, 3, 4, 5], order='C')
print(arr.sum(axis=0)) # sum of all elements
print(arr.mean(axis=0)) # mean of all elements
print(arr.std(axis=0)) # standard deviation of all elements
print(arr.var(axis=0)) # variance of all elements
print(arr.min(axis=0)) # minimum value of all elements
print(arr.max(axis=0)) # maximum value of all elements
print(arr.argmin(axis=0)) # index of minimum value
print(arr.argmax(axis=0)) # index of maximum value