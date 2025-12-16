# ============================= Simple logging decorator =======================

# Define a decorator that logs when a function is called
def log_decorator(func):
    # The wrapper function wraps the original function
    def wrapper(*args, **kwargs):
        # Print the function name before executing
        print(f"Calling {func.__name__}()")
        
        # *args → allows any number of positional arguments
        # **kwargs → allows any number of keyword arguments
        # Call the original function with the same arguments and return the result
        return func(*args, **kwargs)
    
    # Return the wrapper so the decorator can be applied
    return wrapper


# ============================= Example 1 =============================

# Apply the decorator to add1()
@log_decorator
def add1(a, b):
    # Function that returns the sum of two numbers
    return a + b

# Call the decorated function
print("Result:", add1(3, 2))   # Output: Calling add1() \n Result: 5


# ============================= Example 2 =============================

# Apply the same decorator to another function
@log_decorator
def add2(num):
    # Function that returns the sum of all numbers in a list
    return sum(num)

# Call the decorated function
print("Result:", add2([1, 2, 3, 4, 5]))  # Output: Calling add2() \n Result: 15
