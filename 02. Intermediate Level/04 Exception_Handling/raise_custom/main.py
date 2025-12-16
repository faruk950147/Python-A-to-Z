# ============================= What is Raise Custom =============================
# 'raise' is used to trigger (or raise) an exception manually.
# You can also create your own "custom exceptions" by defining a new Exception class.
# This is useful when you want to handle specific errors in your own way.

# ============================= Custom Exception Syntax =============================
# class className(Exception):
#     pass 

# ============================= Basic Raise Custom Example =========================

# Step 1: Create a custom exception
class AgeValueError(Exception):
    """Age is not allowed to be less than 18"""
    pass

try:
    age = float(input("Enter a number: "))
    # Step 2: Raise the custom exception
    if age < 18:
        raise AgeValueError("Age is not allowed to be less than 18.")
    else:
        print("Age is allowed: ", age)
# Step 3: Handle the custom exception
except AgeValueError as e:
    print("AgeValueError: ", str(e))
except Exception as e:
    print("Exception: ", str(e))


# Output:
# AgeValueError: Age is not allowed to be less than 18.
