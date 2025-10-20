    # ============================= 1. What is Tuple =============================
# Ordered Collection: Elements in a tuple maintain a specific order.

# Indexed: Each element has a fixed index.

# Immutable: Once created, a tuple cannot be changed. → Methods like sort(), reverse(), pop(), remove() do not work.

# Iterable: Tuples can be iterated using loops (for, while).

# Duplicates Allowed: Tuples can contain multiple identical values.

# Faster than Lists: Tuples are more memory-efficient and faster for access than lists.

# Heterogeneous Data: A tuple can store different types of data together (e.g., int, str, float).

# Fixed Data: Useful for storing fixed-size data.

# Reference & Dynamic Type: Tuples are reference types and dynamically typed in Python.

# Hashable: Because tuples are immutable, they can be used as keys in dictionaries or elements in sets.

# Note: The immutability of tuples makes them safer to use when you don’t want data to change.

# ============================= 2. Basic 3D Tuple =============================
tuple3d = (
    (
        (1, 2, 3),
        (4, 5, 6)
    ),
    (
        (7, 8, 9),
        (10, 11, 12)
    )
)
print("\n3D Tuple:", tuple3d)

# ============================= 3. Tuple Access Functions =============================
print("\nAccessing elements in 3D Tuple:")
print("tuple3d[0]:", tuple3d[0])
print("tuple3d[1]:", tuple3d[1])
print("tuple3d[0][0]:", tuple3d[0][0])
print("tuple3d[0][1]:", tuple3d[0][1])
print("tuple3d[0][0][0]:", tuple3d[0][0][0])
print("tuple3d[1][1][2]:", tuple3d[1][1][2])

# ============================= Tuple Slicing =============================
print("\nSlicing 3D Tuple:")
print("tuple3d[0:2]:", tuple3d[0:2])
print("tuple3d[0:2][1]:", tuple3d[0:2][1])
print("tuple3d[0:2][1][0]:", tuple3d[0:2][1][0])

# ============================= Tuple Add Functions =============================
# Tuples immutable → create new tuple
tuple3d_added = tuple3d + (((13,14,15),(16,17,18)),)
print("\nTuple after adding new 2D tuple:", tuple3d_added)

# ============================= Tuple Modify Functions =============================
# Tuples immutable → cannot modify in-place
# Can create new tuples
tuple3d_sorted = tuple(tuple(sorted(sub)) for sub2d in tuple3d for sub in sub2d)
print("\nFlattened and sorted elements of tuple3d:", tuple3d_sorted)

# ============================= Tuple Delete Functions =============================
# Tuples immutable → cannot delete individual elements
# Can delete the entire tuple
tuple_temp = tuple3d
del tuple_temp
# print(tuple_temp)  # ❌ NameError, tuple deleted

# ============================= Tuple Loop Functions =============================
print("\nLooping through 3D Tuple:")
for sub2d in tuple3d:
    for sub in sub2d:
        for item in sub:
            print(item, end=" ")
        print()
    print("--- End of 2D slice ---")

# ============================= Tuple Comprehension Functions =============================
# Tuple comprehension → use tuple() on generator
squares = tuple(x**2 for x in range(10))
even = tuple(x for x in range(10) if x % 2 == 0)
chars = tuple(c.upper() for c in "python")
print("\nSquares:", squares)
print("Even numbers:", even)
print("Chars:", chars)
