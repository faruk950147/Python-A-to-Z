# ============================= what is comprehensions =============================
# Comprehensions are a concise way to create lists, dictionaries, and sets.
# It is a way to create a new list by applying an expression to each element of an iterable.
# It is a way to create a new dictionary by applying an expression to each key-value pair of a dictionary.
# It is a way to create a new set by applying an expression to each element of a set.

# ============================= list comprehensions =============================
# List comprehensions are a concise way to create lists.
# It is a way to create a new list by applying an expression to each element of an iterable.
# It is a way to create a new list by applying an expression to each element of a list.
# It is a way to create a new list by applying an expression to each element of a tuple.
# It is a way to create a new list by applying an expression to each element of a set.
# It is a way to create a new list by applying an expression to each element of a dictionary.

# syntax list comprehensions
# [expression for item in iterable]

# 1. Example
list = [i for i in range(10)] # it's a list of numbers from 0 to 9
print(list)

# 2. Example
list = [i * i for i in range(10)] # it's a list of squares of numbers from 0 to 9
print(list)

# 3. Example
list = [i * i for i in range(10) if i % 2 == 0] # it's a list of squares of even numbers from 0 to 9
print(list)

list = [i + i for i in range(10) if i % 2 != 0] # it's a list of squares of odd numbers from 0 to 9
print(list)

# ============================= dictionary comprehensions =============================
# Dictionary comprehensions are a concise way to create dictionaries.
# It is a way to create a new dictionary by applying an expression to each key-value pair of a dictionary.
# It is a way to create a new dictionary by applying an expression to each key-value pair of a list.
# It is a way to create a new dictionary by applying an expression to each key-value pair of a tuple.
# It is a way to create a new dictionary by applying an expression to each key-value pair of a set.
# It is a way to create a new dictionary by applying an expression to each key-value pair of a dictionary.

# 1. Example
dict = {i: i * i for i in range(10)} # it's a dictionary of squares of numbers from 0 to 9
print(dict)

# 2. Example
dict = {i: i * i for i in range(10) if i % 2 == 0} # it's a dictionary of squares of even numbers from 0 to 9
print(dict)

# 3. Example
dict = {i: i * i for i in range(10) if i % 2 != 0} # it's a dictionary of squares of odd numbers from 0 to 9
print(dict)



# ============================= set comprehensions =============================
# Set comprehensions are a concise way to create sets.
# It is a way to create a new set by applying an expression to each element of an iterable.
# It is a way to create a new set by applying an expression to each element of a list.
# It is a way to create a new set by applying an expression to each element of a tuple.
# It is a way to create a new set by applying an expression to each element of a set.
# It is a way to create a new set by applying an expression to each element of a dictionary.

# 1. Example
set = {i for i in range(10)} # it's a set of numbers from 0 to 9
print(set)

# 2. Example
set = {i * i for i in range(10)} # it's a set of squares of numbers from 0 to 9
print(set)

# 3. Example
set = {i * i for i in range(10) if i % 2 == 0} # it's a set of squares of even numbers from 0 to 9
print(set)

set = {i + i for i in range(10) if i % 2 != 0} # it's a set of squares of odd numbers from 0 to 9
print(set)
