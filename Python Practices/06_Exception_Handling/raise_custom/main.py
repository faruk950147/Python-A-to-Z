# ============================= What is Raise Custom =============================
# 'raise' is used to trigger (or raise) an exception manually.
# You can also create your own "custom exceptions" by defining a new Exception class.
# This is useful when you want to handle specific errors in your own way.

# ============================= Custom Exception Syntax =============================
# class className(Exception):
#     pass
# raise className("Something went wrong!")

# ============================= Basic Raise Custom Example =========================

# Step 1: Create a custom exception
class AgeValueError(Exception):
    """Raised when something specific goes wrong"""
    pass

# Step 2: Use the custom exception
def check_age(age):
    if age < 18 :
        # Step 3: Raise the custom exception
        raise AgeValueError(f"Age is not allowed: {age}")
    return age

# Step 4: Handle the exception
try:
    check_age(15)
except AgeValueError as e:
    print(f"AgeValueError: {e}")

# Output:
# AgeValueError: Age is not allowed: 15
