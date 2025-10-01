# Great! Let’s go over types of variables and how they are used in programming. I’ll use Python examples, but the concept is similar in most languages.

# 1. Integer (int)
# Stores whole numbers (no decimal).

age = 25
year = 2025
print(age)
print(year)

# 2. Float (float)
# Stores decimal numbers.

height = 5.9
price = 99.99
print(height)
print(price)

# 3. Decimal (float)
# Stores decimal numbers.

height = 5.9
price = 99.99
print(height)
print(price)

# 4. Boolean (bool)
# Stores True or False values.

is_student = True
has_passed = False
print(is_student)
print(has_passed)

# 5. String (str)
# Stores text.

name = "Faruk"
city = 'Dhaka'
print(name)
print(city)

# 6. List (list)
# Stores multiple values in order (like an array).

fruits = ["apple", "banana", "mango"]
numbers = [1, 2, 3, 4]
print(fruits)
print(numbers)

# 7. Dictionary (dict)
# Stores data as key-value pairs.

student = {"name": "Faruk", "age": 20, "city": "Dhaka"}
print(student)

# 8. Tuple (tuple)
# Stores multiple values in order (like an array), but immutable (cannot be changed).

coordinates = (10, 20)
print(coordinates)

# 9. Set (set)
# Stores unique values (no duplicates).

unique_numbers = {1, 2, 3, 4, 5}
print(unique_numbers)

# 10. None (NoneType)
# Represents the absence of a value.

value = None
print(value)



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


# 11. Variable Rules

# Name must start with a letter or _ (underscore), not a number.

# Names can contain letters, numbers, or _.

# Cannot use Python keywords (like if, for, class).

# Case-sensitive (age ≠ Age).

# Tip: Variables are flexible. You can change their value anytime: