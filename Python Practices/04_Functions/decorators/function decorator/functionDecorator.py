from functools import wraps
# ============================= What is decorator ==============================
# A decorator is a function that takes another function as an argument,
# adds or modifies functionality, and returns a new function.
# It is mainly used to modify or extend the behavior of a function or class
# without changing its actual code.

# A decorator always takes exactly ONE argument — the function it decorates.


# ============================= Function as an argument =========================
def decorator(func, word):
    func(word)

def display(word):
    print("Hello", word)

decorator(display, "World")


# ============================= Basic Function based decorator ==================
def outer_function(func):       # <-- outer function takes ONE argument (the function)
    def inner_function(word):       # <-- inner function (wrapper)
        print("Before function call")
        func(word)                  # <-- calling the original function
        print("After function call")
    return inner_function       # <-- return the inner function

@outer_function
def say_hello(word):
    print("Hello", word)

say_hello("World")

def decorator_func(word):
    def real_decorator(func):
        def wrapper(message):
            print("Before function call")
            func(word)
            print("After function call")
        return wrapper
    return real_decorator


@decorator_func("Python")  # if we pass argument here, it will be passed to the inner function
def say_hello(name):
    print("Hello", name)

say_hello("World")



# ============================= Decorator with *args and **kwargs ================
def decorator_args(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        for arg in args:
            print("Positional arg:", arg)
        for key, value in kwargs.items():
            print("Keyword arg:", key, "=", value)
        func(*args, **kwargs)
        print("Something is happening after the function is called.")
    return wrapper

@decorator_args
def say_hello_args(name, age):
    print("Hello", name, "you are", age, "years old.")

say_hello_args("John", 30)


# ============================= Multiple decorators ============================
def deco1(func):
    def wrapper():
        print("Deco1 Before function call")
        func()
        print("Deco1 After function call")
    return wrapper

def deco2(func):
    def wrapper():
        print("Deco2 Before function call")
        func()
        print("Deco2 After function call")
    return wrapper

@deco1
@deco2
def test():
    print("Function Body")

test()


# ============================= Decorator with arguments =======================
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

greet("Faruk")


# ============================= Decorator with multiple parameters =============
def repeat_n_times(n):
    def decorator(func):
        def wrapper(a, b):
            for _ in range(n):
                func(a, b)
        return wrapper
    return decorator

@repeat_n_times(3)
def greet_two(a, b):
    print(f"Hello, {a} {b}!")

greet_two("Faruk", "Ahmed")


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


# ============================= Practical use cases ============================
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
        result = func(x)
        cache[x] = result
        return result
    return wrapper

@cached
def square(n):
    print("Calculating...")
    return n * n

print(square(4))
print(square(4))


# ---------- Timing Example ----------
import time

def timing(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end-start:.4f} seconds")
        return result
    return wrapper

@timing
def slow_function():
    time.sleep(1)
    print("Done")

slow_function()
