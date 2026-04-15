# FULL DECORATOR CODE (with arguments)
from functools import wraps

# Step 1: Decorator factory (arguments নেয়)
def decorator_with_args(arg1, arg2, arg3):
    # Step 2: Actual decorator (function নেয়)
    def decorator(func):
        # Step 3: Wrapper (real execution control করে)
        @wraps(func)
        def wrapper(*args, **kwargs):

            # decorator arguments print
            print(f"Decorator args: {arg1}, {arg2}, {arg3}")

            # original function call
            result = func(*args, **kwargs)

            return result

        return wrapper

    return decorator


# Step 4: Using decorator
@decorator_with_args("Hello", "World", "!")
def greet(name):
    print(f"Hello, {name}")


# Step 5: Function call
greet("Alice")

'''
# এখন একদম সহজভাবে Flow বুঝো
# Step 1: decorator create হয়
# decorator_with_args("Hello", "World", "!")

# এটা return করে একটা decorator

# Step 2: function decorate হয়
# @decorator
# def greet(name)

# মানে:

greet = decorator(greet)
# Step 3: wrapper তৈরি হয়

# wrapper আসলে function replace করে

# Step 4: function call করলে কী হয়?
greet("Alice")

# actually run হয়:

# wrapper("Alice")
# FINAL OUTPUT
print("Decorator args: Hello, World, !")
print("Hello, Alice")
# এক লাইনে পুরো concept

# decorator_with_args = decorator বানায়
# decorator = function wrap করে
# wrapper = real execution চালায়

# মনে রাখার সহজ trick
# Factory → Decorator → Wrapper → Function
'''

