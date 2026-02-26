import numpy as np
"""
order: 'C' (row-major), 'F' (column-major), 'A' (Fortran if memory-contiguous, else C), 'K' (as stored)
axis: 0 (down rows), 1 (across columns)

"""

# Create a 1D array
# arr = np.array([1, 2, 3, 4, 5], order='C')
# print(arr.sum(axis=0)) # sum of all elements
# print(arr.mean(axis=0)) # mean of all elements
# print(arr.std(axis=0)) # standard deviation of all elements
# print(arr.var(axis=0)) # variance of all elements
# print(arr.min(axis=0)) # minimum value of all elements
# print(arr.max(axis=0)) # maximum value of all elements
# print(arr.argmin(axis=0)) # index of minimum value
# print(arr.argmax(axis=0)) # index of maximum value


# Create a 1D array and convert it to 2D
# np.newaxis means add a new axis at that position (row or column) at that position
# : means all elements
# [np.newaxis, :] means add a new axis at position 0 (row) and select all columns
# arr_2d = np.array([1, 2, 3, 4, 5])
# print(arr_2d[np.newaxis, :])

# Convert to column vector
# what is column vector? A column vector is a matrix with one column and multiple rows
# example = np.array([
#     [1], 
#     [2], 
#     [3], 
#     [4], 
#     [5]
# ]) it means 5 rows and 1 column
# [:, np.newaxis] means select all rows and add a new axis at position 1 (column)

# print(arr_2d[:, np.newaxis])
arr_1d = np.array([1, 2, 3, 4, 5])

expand_dims = np.expand_dims(arr_1d, axis=0)
print(expand_dims)