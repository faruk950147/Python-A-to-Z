import numpy as np

# 1. Start with an empty array
a = np.array([])
print("Initial array:", a)  # []

# 2. Append elements
a = np.append(a, 1)
a = np.append(a, 2)
a = np.append(a, [3, 4])
print("After appending:", a)  # [1. 2. 3. 4]

# 3. Insert elements at specific positions
a = np.insert(a, 0, 5)  # insert 5 at index 0
a = np.insert(a, 2, 6)  # insert 6 at index 2
print("After inserting:", a)  # [5. 1. 6. 2. 3. 4]

# 4. Sort the array (returns a new sorted array)
a_sorted = np.sort(a)
print("Sorted array:", a_sorted)  # [1. 2. 3. 4. 5. 6.]

# 5. argsort (indices that would sort the array)
a_indices = np.argsort(a)
print("Indices that would sort a:", a_indices)  
# Example: If a = [5. 1. 6. 2. 3. 4], output: [1 3 4 5 0 2]

# 6. lexsort (sort by multiple keys)
# Suppose we have two keys: secondary = [1,2,3], primary = [4,5,6]
keys = ([1, 2, 3], [4, 5, 6])
lex_indices = np.lexsort(keys)
print("Lexsort indices:", lex_indices)  # [0 1 2]

# 7. searchsorted (find insertion index in a sorted array)
# Must use a sorted array
idx = np.searchsorted(a_sorted, 3)
print("Index to insert 3:", idx)  # 2

# 8. partition (partial sort: elements before k are smaller, after k are larger)
# Here, k=2 (3rd position)
a_partitioned = np.partition(a, 2)
print("Partitioned array (k=2):", a_partitioned)  
# Output may look like [1. 2. 3. 5. 6. 4.] — first 3 elements are the smallest 3 in any order

# Summary
print("\nFinal Results:")
print("Original array:", a)
print("Sorted array:", a_sorted)
print("Argsort indices:", a_indices)
print("Lexsort indices:", lex_indices)
print("Searchsorted index for 3:", idx)
print("Partitioned array:", a_partitioned)