import numpy as np

a = np.array([1, 2])
b = np.array([3, 4])

# Concatenate arrays
print(np.concatenate((a, b)))
print(np.concatenate((a, b), axis=0))

# Vertical stacking
print(np.vstack((a, b)))

# Horizontal stacking
print(np.hstack((a, b)))

# Split arrays
print(np.split(a, 2))

# Array manipulation
print(np.resize(a, (2, 2)))

# Array manipulation
a = np.array([1, 2, 3, 4])
print(np.reshape(a, (2, 2)))
# Output:
# [[1 2]
#  [3 4]]