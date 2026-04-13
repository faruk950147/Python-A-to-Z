# ============================= 1. What is List =============================
# → List is a collection of items in a specific order
# → Duplicate items allowed (not unique)
# → List is mutable (change possible)
# → Python 3.7+ maintains insertion order
# → Each item is indexed (0-based)
# → List is iterable (loop possible)
# → Reference type, dynamic type
# → Internally implemented as dynamic array

# → Common List Methods
# append()   → add element at end
# extend()   → add multiple elements at end
# insert()   → add element at specific index
# remove()   → remove element by value
# pop()      → remove element by index (default last)
# clear()    → remove all elements
# index()    → find index of element
# count()    → count occurrences
# sort()     → sort list (in-place)
# reverse()  → reverse list (in-place)
# copy()     → shallow copy
# len(list)  → length of list
# max(list)  → maximum value
# min(list)  → minimum value
# sum(list)  → sum of numeric elements
# sorted(list) → returns new sorted list
# any(list)  → True if any element is True
# all(list)  → True if all elements are True
# enumerate(list) → index + value pairs
# zip(list1, list2) → combine multiple lists
# list(iterable) → convert iterable to list


# ============================= 2. Basic List 1D =============================
list1d = [1, 2, 3, 4, 5]
list1d = list(range(1, 6))
list1d = list("12345")


# ============================= 3. List Access & Slicing =============================

list1 = ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']

print(list1[0])     # first element
print(list1[-1])    # last element

# slicing
print(list1[1:3])    # ['e', 'l']
print(list1[:3])     # ['H','e','l']
print(list1[0:])     # full list
print(list1[:])      # copy of list
print(list1[::2])    # step slicing
print(list1[::-1])   # reverse list

# negative indexing
print(list1[-1])     # last element
print(list1[-2:])    # last 2 elements
print(list1[:-2])    # all except last 2


# ============================= 4. List Add Functions =============================

list1 = [1, 2, 3]

list1.append(6)          # add at end
list1.extend([7, 8, 9])  # add multiple elements
list1.insert(0, 0)       # add at index

print(list1)


# ============================= 5. List Modify Functions =============================

list1 = [3, 1, 4, 2]

list1.sort()      # ascending
list1.reverse()   # reverse order

copy_list = list1.copy()  # shallow copy

print(list1)
print(copy_list)


# ============================= 6. List Delete Functions =============================

list1 = [1, 2, 3, 4, 5]

list1.remove(3)   # remove by value
list1.pop()       # remove last element
list1.pop(1)      # remove index
# list1.clear()    # remove all elements


# ============================= 7. Looping List =============================

list1 = [1, 2, 3, 4, 5]

# by index
for i in range(len(list1)):
    print(list1[i])

# direct iteration
for item in list1:
    print(item)


# ============================= 8. List Comprehension =============================

squares = [x**2 for x in range(10)]
even = [x for x in range(10) if x % 2 == 0]
chars = [c.upper() for c in "python"]

print(squares)
print(even)
print(chars)


# ============================= 9. List Condition Functions =============================

list1 = [1, 2, 3, 4, 5]

print(any(x > 3 for x in list1))   # True
print(all(x > 0 for x in list1))   # True
print(max(list1))                  # 5
print(min(list1))                  # 1
print(sum(list1))                  # 15