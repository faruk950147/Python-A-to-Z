import numpy as np

# arr = np.array([1, 2, 3, 4, 5])
# print(arr.dtype)

# arr = np.array([1, 2, 3, 4, 5], dtype=np.float64)
# print(arr.dtype)

# arr = np.array([1, 2, 3, 4, 5], dtype=np.int32)
# print(arr.dtype)

# arr = np.array([1, 2, 3, 4, 5], dtype=np.int16)
# print(arr.dtype)

# arr = np.array([1, 2, 3, 4, 5], dtype=np.int8)
# print(arr.dtype)

# new_arr = np.array([1, 2, 3, 4, 5], dtype=np.float64)
# print(new_arr.dtype)


# astype() this method cannot change the data type of an array original array
arr = np.array([1, 2, 3, 4, 5])
print(arr.dtype)
new_arr = arr.astype(np.float64)
print(arr)
print(new_arr)
print(arr.dtype)
print(new_arr.dtype)
