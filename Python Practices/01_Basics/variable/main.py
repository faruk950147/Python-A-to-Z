"""
Variable Names
A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume).

Rules for Python variables:

A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.
"""
# Legal Variable
myvar = "John" # camel case
my_var = "John" # snake case
_my_var = "John" # snake case
myVar = "John" # camel case
MYVAR = "John" # camel case
myvar2 = "John" # camel case

# Print
print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)

# Illegal Variable
# 2myvar = "John" # start with number
# my-var = "John" # contain special character
# my var = "John" # contain special character

# Many Values to Multiple Variables
# Python allows you to assign values to multiple variables in one line:

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)


# One Value to Multiple Variables
# You can assign the same value to multiple variables in one line:
x = y = z = "Orange"
print(x)
print(y)
print(z)


# Unpack a Collection
# If you have a collection of values in a list, tuple etc. 
# Python allows you to extract the values into variables. This is called unpacking.
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

fruits1 = ("apple", "banana", "cherry")
x, y, z = fruits1
print(x)
print(y)
print(z)

#  In the print() function, you output multiple variables, separated by a comma:

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)