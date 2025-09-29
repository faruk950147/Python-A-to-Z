# Great! Let’s go over types of variables and how they are used in programming. I’ll use Python examples, but the concept is similar in most languages.

# 1. Integer (int)

# Stores whole numbers (no decimal).

# age = 25
# year = 2025

# 2. Float (float)

# Stores decimal numbers.

# height = 5.9
# price = 99.99

# 3. String (str)

# Stores text, enclosed in quotes.

# name = "Faruk"
# city = 'Dhaka'

# 4. Boolean (bool)

# Stores True or False.

# is_student = True
# has_passed = False

# 5. List

# Stores multiple values in order (like an array).

# fruits = ["apple", "banana", "mango"]
# numbers = [1, 2, 3, 4]

# 6. Dictionary (dict)

# Stores data as key-value pairs.

# student = {"name": "Faruk", "age": 20, "city": "Dhaka"}

# 7. Variable Rules

# Name must start with a letter or _ (underscore), not a number.

# Names can contain letters, numbers, or _.

# Cannot use Python keywords (like if, for, class).

# Case-sensitive (age ≠ Age).

# Tip: Variables are flexible. You can change their value anytime:

# age = 25
# age = 26  # Changed

# constant
# PI = 3.14
# PI = 3.14159
# PI = 3.141592653589793
# PI = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679

# 8. Tuple

# Stores multiple values in order (like an array), but immutable (cannot be changed).

# coordinates = (10, 20)

# 9. Set

# Stores unique values (no duplicates).

# unique_numbers = {1, 2, 3, 4, 5}

# 10. None

# Represents the absence of a value.

# value = None

# 11. Type

# Returns the type of a variable.

# print(type(age))  # <class 'int'>
# print(type(height))  # <class 'float'>
# print(type(name))  # <class 'str'>
# print(type(is_student))  # <class 'bool'>
# print(type(fruits))  # <class 'list'>
# print(type(student))  # <class 'dict'>
# print(type(coordinates))  # <class 'tuple'>
# print(type(unique_numbers))  # <class 'set'>
# print(type(value))  # <class 'NoneType'>


# ======================= memory location =======================
a = 10 # same memory location because of small int and same value
b = 10 # same memory location because of small int and same value
print(id(a))
print(id(b))
print(id(a) == id(b))

# ======================= memory location =======================
a = 10 # different memory location because of large int and different value
b = 20 # different memory location because of large int and different value
print(id(a))
print(id(b))
print(id(a) == id(b))