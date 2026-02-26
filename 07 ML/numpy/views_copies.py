
import numpy as np

# views
# arr = np.array([1, 2, 3])
# view = arr.view()
# view = arr[1:3]

# change the view
# view[0] = 10
# print("Original array:", arr)
# print("View:", view)

# copies
arr = np.array([1, 2, 3])
# copy = arr.copy()
copy = arr[0:2].copy()

print("Original array:", arr)
copy[0] = 10
print("Copy:", copy)