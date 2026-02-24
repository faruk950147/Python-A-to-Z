import numpy as np

# Create an array
# print("One Dimensional Array")
# arr = np.array([1, 2, 3, 4, 5])
# print("Array:", arr)
# print("Data type:", arr.dtype)
# print("Number of dimensions:", arr.ndim)
# print("Shape:", arr.shape)
# print("Size:", arr.size)
# print("Item size:", arr.itemsize)
# print("Data:", arr.data)
# print("End One Dimensional Array")


# create a matrix
# print("\nTwo Dimensional Array")
# mat = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print("Matrix:", mat)
# print("Data type:", mat.dtype)
# print("Number of dimensions:", mat.ndim)
# print("Shape:", mat.shape)
# print("Size:", mat.size)
# print("Item size:", mat.itemsize)
# print("Data:", mat.data)
# print("End Two Dimensional Array")

# create a 3D array
# (2 blocks) two blocks
#    ↓
# (3 rows) three rows
#    ↓
# (4 columns) four columns

# print("\nThree Dimensional Array")
# c = np.arange(24).reshape(2,3,4)
# print(c)
# print("End Three Dimensional Array")

# Zeros
# print(np.zeros((3,4)))
# Ones
# print(np.ones((2,3)))
# Empty
# print(np.empty((2,2)))
# Range
# print(np.arange(0,10,2))
# Linspace (Best for float)
# print(np.linspace(0,2,9))

# Basic Operations (Without Loop)
# Elementwise
a = np.array([20,30,40,50])
b = np.arange(4)

a - b
b**2
np.sin(a)
# Matrix Multiplication
A @ B
A.dot(B)
# Sum / Min / Max
a.sum()
a.min()
a.max()
# Axis 
b.sum(axis=0)   # column sum
b.sum(axis=1)   # row sum
# Universal Functions (ufunc)
np.exp(a)
np.sqrt(a)
np.add(a,b)

# all element automatically apply 

# Indexing & Slicing
# 1D
a[2]
a[2:5]
a[::-1]
# 2D
b[1,2]
b[:,1]
b[1:3,:]
# Ellipsis (...)
c[1,...]
c[...,2]
# Shape Change
a.reshape(3,4)
a.ravel()
a.T
# -1 use
a.reshape(3,-1)
# Stack & Split
# Stack
np.vstack((a,b))
np.hstack((a,b))
# Split
np.hsplit(a,3)
np.vsplit(a,2)
# Copy vs View (very important)
# No Copy
b = a
# View
c = a.view()
# Deep Copy
d = a.copy()
# Broadcasting (Magic Feature)

# Broadcasting that small array to big array with automatic match.

# Rule:
# Dimension equal     
# Size 1 -> repeat

# Example:

a = np.array([1,2,3])
b = 10

a + b
# Boolean Indexing
a[a > 4]

# Assignment
a[a > 4] = 0