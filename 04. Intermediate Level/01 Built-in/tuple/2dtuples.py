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
# =================== What is Tuple ===================

# Tuple is a collection of items. 
# Tuple is ordered, unchangeable, and allows duplicate values.
# Tuple is written with round brackets.
# when the run output show ordered, unchangeable, and allows duplicate values, it means that the tuple is ordered, unchangeable, and allows duplicate values.
# Tuple is immutable (change not possible) but its items are immutable only if they themselves are immutable.
# Tuple is iterable (loop possible).
tuple = (1,2,3, [4,5,6]) # itq is mutable (change possible) because its item is mutable.

# ============================= 2. Basic 2D Tuple =============================
tuple2d = ((1, 2, 3), (4, 5, 6))
print("\n2D Tuple:", tuple2d)

# ============================= 3. Tuple Access Functions =============================
print("\nAccessing elements in 2D Tuple:")
print("tuple2d[0]:", tuple2d[0])
print("tuple2d[1]:", tuple2d[1])
print("tuple2d[0][0]:", tuple2d[0][0])
print("tuple2d[0][1]:", tuple2d[0][1])
print("tuple2d[0][2]:", tuple2d[0][2])
print("tuple2d[1][0]:", tuple2d[1][0])
print("tuple2d[1][1]:", tuple2d[1][1])
print("tuple2d[1][2]:", tuple2d[1][2])

# Slice example
print("\nSlicing 2D Tuple:")
print("tuple2d[0:2]:", tuple2d[0:2])
print("tuple2d[0:2][0]:", tuple2d[0:2][0])
print("tuple2d[0:2][1]:", tuple2d[0:2][1])

# ============================= 4. Tuple "Add" Functions =============================
# Tuples are immutable → we cannot use append/extend/insert
# We can create a new tuple
tuple2d_added = tuple2d + ((7, 8, 9), (10, 11, 12))
tuple2d_added = ((0, 0, 0),) + tuple2d_added  # prepend
print("\nTuple after adding elements:", tuple2d_added)

# ============================= 5. Tuple Modify Functions =============================
# Tuples are immutable → cannot sort/reverse in place
tuple2d_mod = ((3, 2, 1), (6, 5, 4))
tuple2d_sorted = tuple(sorted(tuple2d_mod[0])), tuple(sorted(tuple2d_mod[1]))
tuple2d_reversed = tuple(reversed(tuple2d_mod[0])), tuple(reversed(tuple2d_mod[1]))
tuple2d_copy = tuple(tuple2d_mod)
print("\nOriginal tuple:", tuple2d_mod)
print("Sorted tuple:", tuple2d_sorted)
print("Reversed tuple:", tuple2d_reversed)
print("Copied tuple:", tuple2d_copy)

# ============================= 6. Tuple Loop Functions =============================
print("\nLooping through 2D tuple:")
for row in tuple2d:
    for col in row:
        print(col, end=" ")
    print()

# ============================= 7. Tuple Comprehension Functions =============================
# Tuple comprehension → generator expression → convert to tuple
squares = tuple(x**2 for x in range(10))
even = tuple(x for x in range(10) if x % 2 == 0)
chars = tuple(c.upper() for c in "python")
print("\nSquares:", squares)
print("Even numbers:", even)
print("Chars:", chars)
