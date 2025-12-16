from functools import wraps
import time

# ============================= What is a Decorator ==============================
# A decorator is a function that takes another function as an argument,
# adds or modifies functionality, and returns a new function.
# It allows you to extend or modify the behavior of functions or methods
# without changing their code.

# ============================= functools.wraps Example ========================
def my_decorator_wrap(func):
    @wraps(func)
    def wrapper():
        """Wrapper function"""
        print("Inside wrapper")
        return func()
    return wrapper

@my_decorator_wrap
def say_wrap():
    """Original function"""
    print("Hi from wrap")

say_wrap()
print("Function name:", say_wrap.__name__)
print("Docstring:", say_wrap.__doc__)
