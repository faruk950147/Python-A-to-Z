# ============================= Calculation Validator Decorator ===============================

def is_validator(func):
    def wrapper(*args, **kwargs):
        # Check all positional arguments
        for num in args:
            if num < 0:
                # Just raise the error directly (no return needed)
                raise ValueError("Negative arguments are not allowed")

        # Check all keyword argument values
        for num in kwargs.values():
            if num < 0:
                raise ValueError("Negative arguments are not allowed")

        # If all values are valid (non-negative), call the original function
        return func(*args, **kwargs)
    
    # Return the wrapper function so the decorator can work
    return wrapper





# ============================= Example Function ===============================

@is_validator
def add(*args, **kwargs):
    # Print sum of positional and keyword arguments
    return sum(args) + sum(kwargs.values())


print(add(1,2))
print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, a=1, b=2, c=3, d=4, e=5, f=6, g=7, h=8, i=9, j=10))
