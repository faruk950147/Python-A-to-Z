import numpy as np
arr = np.array([1,2,3,4])

# Create 5 zeros

np.zeros(5)

# Create 3x3 ones matrix

np.ones((3,3))

# Create numbers 0–9

np.arange(10)

# Create 10 numbers between 0–1

np.linspace(0,1,10)

# Find shape

arr.shape

# Find dimension

arr.ndim

# Reshape into 2x2

arr.reshape(2,2)

# Flatten array

arr.flatten()

# Find max value

np.max(arr)
# Level 2: Intermediate (26–60)

# Find mean

np.mean(arr)

# Find standard deviation

np.std(arr)

# Boolean filtering (>5)

arr[arr > 5]

# Sort array

np.sort(arr)

# Get index of max

np.argmax(arr)

# Matrix multiplication

np.dot(a,b)

# Transpose

a.T

# Stack vertically

np.vstack((a,b))

# Unique values

np.unique(arr)

# Replace values >5 with 0

arr[arr>5] = 0
# Level 3: Advanced (61–100+)

# Create 5x5 identity

np.eye(5)

# Solve linear equation

np.linalg.solve(A,b)

# Determinant

np.linalg.det(A)

# Eigenvalues

np.linalg.eig(A)

# Broadcasting example

a = np.array([1,2,3])
b = np.array([[1],[2],[3]])
a + b

# Cumulative sum

np.cumsum(arr)

# Correlation matrix

np.corrcoef(data)

# Normalize data

(arr - np.mean(arr)) / np.std(arr)

# Random shuffle

np.random.shuffle(arr)

# Create meshgrid

x = np.linspace(0,5,10)
y = np.linspace(0,5,10)
X,Y = np.meshgrid(x,y)


# PART 2: NumPy with Real Machine Learning Examples

# 1. Linear Regression (From Scratch)
X = np.array([1,2,3,4,5])
Y = np.array([2,4,6,8,10])

w = np.sum(X*Y) / np.sum(X**2)

y_pred = w * X

# 2. Gradient Descent
w = 0
lr = 0.01

for i in range(100):
    y_pred = w*X
    error = y_pred - Y
    grad = np.mean(error * X)
    w = w - lr*grad

# 3. Logistic Regression Sigmoid
def sigmoid(z):
    return 1/(1+np.exp(-z))

# 4. Image as NumPy Array

# Image = 3D array (height × width × channels)

# image.shape

# PART 3: Advanced NumPy (Deep Dive)

# Broadcasting Explained

# Rules:
# Dimensions must match

# Or one must be 1

# Comparison starts from right

a = np.array([[1,2,3]])
b = np.array([[1],[2],[3]])

a + b

# Vectorization (Why NumPy Fast?)

# Python Loop

result = []
for i in range(len(arr)):
    result.append(arr[i]*2)

# NumPy Vectorized

arr * 2

# Reason:

# Written in C

# SIMD optimized

# Memory contiguous

# Memory Layout
arr.flags
arr.strides

# C-order vs Fortran-order

# PART 4: NumPy + Matplotlib Full Guide

# About Libraries

# NumPy

# Matplotlib

# Line Plot
import matplotlib.pyplot as plt

x = np.linspace(0,10,100)
y = np.sin(x)

plt.plot(x,y)
plt.show()

# Bar Chart
plt.bar(['A','B','C'], [10,20,15])
plt.show()

# Histogram
data = np.random.randn(1000)
plt.hist(data)
plt.show()

# Scatter Plot
x = np.random.rand(100)
y = np.random.rand(100)
plt.scatter(x,y)
plt.show()