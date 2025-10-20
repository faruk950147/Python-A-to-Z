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
# ============================= 2. Basic Tuple =============================
tuple1 = (1, 2, 3)
tuple2 = tuple([1, 2, 3])
tuple3 = tuple("abc")
tuple4 = tuple(range(1, 5))
tuple5 = tuple()
tuple_single = (1,)  # Single element tuple

print("\n================ Basic Tuples ================")
print("tuple1:", tuple1)
print("tuple2:", tuple2)
print("tuple3:", tuple3)
print("tuple4:", tuple4)
print("tuple5:", tuple5)
print("tuple_single:", tuple_single)

# ============================= 3. Tuple Access & Slicing =============================
tuple_str = ('H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd')
print("\n================ Tuple Slicing ================")
print("tuple_str[1:3]:", tuple_str[1:3])
print("tuple_str[:3]:", tuple_str[:3])
print("tuple_str[0:]:", tuple_str[0:])
print("tuple_str[:]:", tuple_str[:])
print("tuple_str[::]:", tuple_str[::])
print("tuple_str[::2]:", tuple_str[::2])
print("tuple_str[::3]:", tuple_str[::3])

# ============================= Negative Indexing =============================
print("\n================ Negative Indexing ================")
print("tuple_str[-1]:", tuple_str[-1])
print("tuple_str[-2:]:", tuple_str[-2:])
print("tuple_str[:-2]:", tuple_str[:-2])
print("tuple_str[-2:-1]:", tuple_str[-2:-1])
print("tuple_str[-2:-3]:", tuple_str[-2:-3])  # empty tuple

# ============================= Tuple Reverse =============================
print("\n================ Tuple Reverse ================")
print("tuple_str[::-1]:", tuple_str[::-1])
print("tuple_str[::-2]:", tuple_str[::-2])
print("tuple_str[::-3]:", tuple_str[::-3])
print("tuple_str[::-4]:", tuple_str[::-4])

# ============================= 4. Tuple "Add" Functions =============================
print("\n================ Tuple Add Functions ================")
tuple_num = (1, 2, 3)
tuple_num = tuple_num + (4, 5)      # New tuple
tuple_num = (0,) + tuple_num        # Prepend
tuple_num = tuple_num + (6,)        # Append single element
tuple_num = tuple_num + tuple([7,8,9])  # Add multiple elements
print("tuple_num (after additions):", tuple_num)

# ============================= 5. Tuple Modify Functions =============================
print("\n================ Tuple Modify Functions ================")
# Tuple immutable → cannot sort, reverse, pop, remove
# But we can create new tuple using sorted or reversed
tuple_mod = (3, 1, 2)
tuple_mod_sorted = tuple(sorted(tuple_mod))
tuple_mod_reversed = tuple(reversed(tuple_mod))
tuple_mod_copy = tuple(tuple_mod)  # Shallow copy
print("Original tuple:", tuple_mod)
print("Sorted tuple:", tuple_mod_sorted)
print("Reversed tuple:", tuple_mod_reversed)
print("Copied tuple:", tuple_mod_copy)

# ============================= 6. Tuple Delete Functions =============================
print("\n================ Tuple Delete Functions ================")
# Tuple immutable → cannot pop, remove, clear
# Only deletion is possible
tuple_del = (1, 2, 3, 4, 5)
del tuple_del
# print(tuple_del)  # This will raise NameError because tuple is deleted

# ============================= 7. Looping Tuple =============================
print("\n================ Looping Tuple ================")
tuple_loop = (1, 2, 3, 4, 5)
for i in range(len(tuple_loop)):
    print("Index loop:", tuple_loop[i])

for val in tuple_loop:
    print("Direct loop:", val)

# ============================= 8. Tuple "Comprehension" =============================
print("\n================ Tuple Comprehension ================")
# Generator expression → convert to tuple
squares = tuple(x**2 for x in range(10))
even = tuple(x for x in range(10) if x % 2 == 0)
chars = tuple(c.upper() for c in "python")
print("Squares:", squares)
print("Even numbers:", even)
print("Chars:", chars)



