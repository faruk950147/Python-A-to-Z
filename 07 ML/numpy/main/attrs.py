import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr)

print("Shape:", arr.shape)
print("Size:", arr.size)
print("Data type:", arr.dtype)
print("Number of dimensions:", arr.ndim)
print("Number of dimensions:", len(arr.shape) == arr.ndim)
