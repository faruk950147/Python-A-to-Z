# Copying in Python: Full Guide

# Python has three main ways to handle copying of objects:

# Assignment (No Copy)

# Shallow Copy

# Deep Copy

# Assignment (No Copy)

# When you assign one variable to another using =, both variables point to the same object.

dict1 = {1: 'one', 2: 'two'}
dict2 = dict1  # assignment, no copy

print(dict1)  # {1: 'one', 2: 'two'}
print(dict2)  # {1: 'one', 2: 'two'}
print(id(dict1), id(dict2))  # same id

dict2[1] = 'ONE'
print(dict1)  # {1: 'ONE', 2: 'two'}


# Both dict1 and dict2 refer to the same object in memory.

# Changes in one will reflect in the other.

# Shallow Copy

# A shallow copy creates a new object, but nested objects inside are still references to the same objects in memory.

# Example using copy()
a = {1: 'one', 2: [10, 20]}
b = a.copy()  # shallow copy

print(a, b)       # {1: 'one', 2: [10, 20]} {1: 'one', 2: [10, 20]}
print(id(a), id(b))  # different ids

b[2].append(30)
print(a, b)       # {1: 'one', 2: [10, 20, 30]} {1: 'one', 2: [10, 20, 30]}


# Top-level dictionary is new (id is different).

# Nested list is shared, so modifying it affects both.

# Deep Copy

# A deep copy duplicates the object and all nested objects recursively.

import copy

dict1 = {1: 'one', 2: [10, 20]}
dict2 = copy.deepcopy(dict1)  # deep copy

dict2[2].append(30)

print(dict1)  # {1: 'one', 2: [10, 20]}
print(dict2)  # {1: 'one', 2: [10, 20, 30]}


# dict2 is completely independent of dict1.

# Safe for nested mutable objects.