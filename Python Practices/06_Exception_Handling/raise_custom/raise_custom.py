# ============================= What is Raise Custom =============================
# 'raise' is used to trigger (or raise) an exception manually.
# You can also create your own "custom exceptions" by defining a new Exception class.
# This is useful when you want to handle specific errors in your own way.

# Structure:
# raise Exception("Error message")

# Custom Exception Example:
# class MyError(Exception):
#     pass
# raise MyError("Something went wrong!")


# ============================= basic raise custom =============================
# Simple examples of raise

try:
    x = int(input("Enter a positive number: "))
    if x < 0:
        raise ValueError("Negative numbers are not allowed.")
    print("You entered:", x)
except ValueError as e:
    print("Error:", e)


# ============================= raise custom =============================
# How to use raise with custom exception classes

# Define a custom exception
class InvalidAgeError(Exception):
    """Custom exception for invalid age."""
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError("You must be at least 18 years old.")
    else:
        print("Access granted!")

try:
    user_age = int(input("Enter your age: "))
    check_age(user_age)
except InvalidAgeError as e:
    print("Custom Error:", e)
except Exception as e:
    print("General Error:", e)


# ============================= practical use cases =============================
# - Data processing: raise custom errors when data format is invalid
# - Business logic: raise specific errors for business rules
# - Algorithm implementation: raise error when conditions are violated

# Example 1: Data processing
class InvalidDataFormat(Exception):
    pass

def process_data(data):
    if not isinstance(data, dict):
        raise InvalidDataFormat("Data must be a dictionary.")
    print("Processing:", data)

try:
    process_data(["not", "a", "dict"])
except InvalidDataFormat as e:
    print("Data Error:", e)


# Example 2: Business logic
class InsufficientBalanceError(Exception):
    pass

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientBalanceError("Insufficient balance for withdrawal.")
    else:
        print("Withdrawal successful. Remaining balance:", balance - amount)

try:
    withdraw(100, 200)
except InsufficientBalanceError as e:
    print("Transaction Error:", e)


# Example 3: Algorithm implementation
class InvalidInputError(Exception):
    pass

def factorial(n):
    if n < 0:
        raise InvalidInputError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

try:
    print(factorial(-5))
except InvalidInputError as e:
    print("Algorithm Error:", e)
