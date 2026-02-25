import numpy as np

a = np.array([])

# Add 1
a = np.append(a, 1)          # [1.]
# Add 2
a = np.append(a, 2)          # [1. 2.]
# Add multiple elements
a = np.append(a, [3, 4])     # [1. 2. 3. 4]
# Insert 5 at index 0
a = np.insert(a, 0, 5)       # [5. 1. 2. 3. 4]
# Insert 6 at index 2
a = np.insert(a, 2, 6)       # [5. 1. 6. 2. 3. 4]

print(a)
# Output: [5. 1. 6. 2. 3. 4.]

