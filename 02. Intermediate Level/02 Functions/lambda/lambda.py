# ============================= What is Lambda Function ==============================
# A lambda function is a small anonymous function defined with the lambda keyword.
# It can take any number of arguments but can only have one expression.
# Syntax: lambda arguments: expression


# ============================= basic lambda ============================================
# Example 1: Lambda with two arguments
add = lambda a, b: a + b
print(add(2, 3))  # Output: 5

# Example 2: Lambda with one argument
square = lambda x: x * x
print(square(4))  # Output: 16


lam = lambda a, b: (a + b, a - b, a * b, a / b)
sum, sub, mul, div = lam(10, 5)
print('Faruk sum:', sum, 'sub:', sub, 'mul:', mul, 'div:', div)


# ============================= lambda vs normal function ===============================
# Normal function
def add_func(a, b):
    return a + b

print(add_func(2, 3))  # Output: 5

# Lambda function (shorter, anonymous)
print((lambda a, b: a + b)(2, 3))  # Output: 5

# Differences:
# - lambda is anonymous (no name needed unless assigned to a variable)
# - lambda is written in one line
# - normal function can have multiple statements


# ============================= lambda with no arguments ================================
no_arg = lambda: "Hello"
print(no_arg())  # Output: Hello


# ============================= lambda with single argument ==============================
add_ten = lambda x: x + 10
print(add_ten(5))  # Output: 15


# ============================= lambda with multiple arguments ===========================
multiply = lambda x, y: x * y
print(multiply(3, 4))  # Output: 12


# ============================= lambda inside functions =================================
def power_function(n):
    return lambda x: x ** n   # local helper function

square = power_function(2)
cube = power_function(3)

print(square(5))  # Output: 25
print(cube(2))    # Output: 8


# ============================= lambda with higher-order functions =======================
nums = [1, 2, 3, 4, 5]

# map()
squared = list(map(lambda x: x ** 2, nums))
print(squared)  # Output: [1, 4, 9, 16, 25]

# filter()
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)  # Output: [2, 4]

# reduce()
from functools import reduce
sum_all = reduce(lambda a, b: a + b, nums)
print(sum_all)  # Output: 15

# sorted() with key
words = ["apple", "banana", "cherry", "date"]
sorted_by_length = sorted(words, key=lambda w: len(w))
print(sorted_by_length)  # Output: ['date', 'apple', 'banana', 'cherry']


# ============================= lambda with conditional expression ======================
check_even = lambda x: "Even" if x % 2 == 0 else "Odd"
print(check_even(5))  # Output: Odd
print(check_even(8))  # Output: Even


# ============================= limitations of lambda ===================================
# - Limited to a single expression
# - Cannot contain multiple statements
# - Not suitable for complex logic
# - Cannot have return, print, or loops directly

# Example of limitation:
# This is NOT allowed inside lambda:
# lambda x: (y = x + 1)   
