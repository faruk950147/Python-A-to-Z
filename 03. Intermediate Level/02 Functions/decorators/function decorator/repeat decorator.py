# ============================= Repeat decorator ===============================

# Outer function that takes 'num' as argument (number of repetitions)
def repeat(num):
    # This is the actual decorator
    def decorator(func):
        # Wrapper function that replaces the original function
        def wrapper(*args, **kwargs):
            for _ in range(num):  # Repeat the function call 'num' times
                # Call the original function with given arguments
                func(*args, **kwargs)
        return wrapper  # Return the wrapper so the decorator works
    return decorator  # Return the decorator itself


# Apply the repeat decorator with argument 3
@repeat(3)
def greet(name):
    # Simple function that prints a greeting
    print(f"Hello, {name}!")

# Call the decorated function
greet("Faruk")
