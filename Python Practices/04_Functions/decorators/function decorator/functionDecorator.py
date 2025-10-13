from functools import wraps
import time

# ============================= What is a Decorator ==============================
# A decorator is a function that takes another function as an argument,
# adds or modifies functionality, and returns a new function.
# It allows you to extend or modify the behavior of functions or methods
# without changing their code.





# ============================= Basic Decorator =================================
def decorator2(func): # <-- decorator function takes ONE argument (the function)
    def wrapper(word): # <-- real actual wrapper function takes ONE argument (the function)
        print("Before function call")
        func(word)
        print("After function call")
    return wrapper

@decorator2
def say_hello(word):
    print("Hello", word)

say_hello("World")


# ============================= Decorator with arguments =======================
def decorator_func(word): # <-- decorator function takes ONE argument (the function)
    def real_decorator(func): # <-- real actual decorator function takes ONE argument (the function)
        def wrapper(message): # <-- wrapper function takes ONE argument (the function)
            print("Before function call")
            func(word)
            print("After function call")
        return wrapper
    return real_decorator

@decorator_func("Python")
def say_hello_arg(name):
    print("Hello", name)

say_hello_arg("World")


# ============================= Decorator with *args and **kwargs ================
def decorator_args(func): # <-- decorator function takes ONE argument (the function)
    def wrapper(*args, **kwargs): # <-- real actual wrapper function takes ONE argument (the function)
        print("Before function call")
        func(*args, **kwargs)
        print("After function call")
    return wrapper

@decorator_args
def say_hello_args(name, age):
    print(f"Hello {name}, you are {age} years old.")

say_hello_args("John", 30)


# ============================= Multiple decorators ============================
def deco1(func):
    def wrapper():
        print("Deco1 Before")
        func()
        print("Deco1 After")
    return wrapper

def deco2(func):
    def wrapper():
        print("Deco2 Before")
        func()
        print("Deco2 After")
    return wrapper

@deco1
@deco2
def test():
    print("Function Body")

test()


# ============================= Repeat decorator ===============================
def repeat(num):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(num):
                func(*args, **kwargs).sum()
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

greet("Faruk")


# ============================= Simple logging decorator =======================
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}()")
        return func(*args, **kwargs)
    return wrapper

@log_decorator
def add(a, b):
    return a + b

print("Result:", add(3, 2))


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


# ============================= Practical Use Cases ============================

# ---------- Authorization Example ----------
def require_admin(func):
    def wrapper(user):
        if user == "admin":
            return func(user)
        else:
            print("Access denied!")
    return wrapper

@require_admin
def view_dashboard(user):
    print(f"{user} is viewing the dashboard")

view_dashboard("admin")
view_dashboard("guest")


# ---------- Caching Example ----------
cache = {}
def cached(func):
    def wrapper(x):
        if x in cache:
            print("Returning from cache")
            return cache[x]
        print("Calculating...")
        result = func(x)
        cache[x] = result
        return result
    return wrapper

@cached
def square(n):
    return n * n

print(square(4))
print(square(4))


# ---------- Timing Example ----------
def timing(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timing
def slow_function():
    time.sleep(1)
    print("Done")

slow_function()
