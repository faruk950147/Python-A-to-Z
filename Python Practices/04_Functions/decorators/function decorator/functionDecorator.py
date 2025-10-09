# import time
# ============================= What is decorator ==============================
# decorator is a function that takes another function as an argument,
# adds some functionality, and returns a new function. 
# It is used to modify the behavior of a function or class.

# # ============================= Function based decorator ==============================
# def decorator(func):
#     def wrapper():
#         print("Before function call")
#         func()
#         print("After function call")
#     return wrapper

# @decorator
# def say_hello():
#     print("Hello")
    
# say_hello()


# ============================= function as an argument =========================
# def greet(func):
#     func()

# def hello():
#     print("Hello World")

# greet(hello)


# ============================= function return function =====================
# def outer():
#     print("I'm outer function")
#     def inner():
#         print("I am inner function")
#     return inner

# f = outer() # that means store and call inner() function
# f()
# outer() # just outer function


# ============================= multiple decorators ==========================
# def deco1(func):
#     def wrapper():
#         print("Deco1 Before function call")
#         func()
#         print("Deco1 After function call")
#     return wrapper

# def deco2(func):
#     def wrapper():
#         print("Deco2 Before function call")
#         func()
#         print("Deco2 After function call")
#     return wrapper

# @deco1
# @deco2
# def test():
#     print("Function Body")
    
# test()


# ============================= decorators with arguments ====================
# def repeat(n):
#     def decorator(func):
#         def wrapper():
#             for _ in range(n):
#                 func()
#         return wrapper
#     return decorator

# @repeat(3)
# def hello_repeat():
#     print("Hello")

# def repeat(n):
#     def decorator(func):
#         def wrapper(*args, **kwargs):   # <-- here argument pass as an argument
#             for _ in range(n):
#                 func(*args, **kwargs)   # <-- here argument pass as an argument
#         return wrapper
#     return decorator



# @repeat(3)
# def greet(name):
#     print(f"Hello, {name}!")
    

# greet("Faruk")

def repeat(n):
    def decorator(func):
        def wrapper(a, b):   # <-- here argument pass as an argument
            for _ in range(n):
                func(a, b)   # <-- here argument pass as an argument
        return wrapper
    return decorator

@repeat(3)
def greet(a, b):
    print(f"Hello, {a} {b}!")
    

greet("Faruk", "Faruk")


def decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@decorator
def add(a, b):
    return a + b

print(add(3, 2))


# ============================= functools.wraps ==============================
# from functools import wraps

# def my_decorator_wrap(func):
#     @wraps(func)
#     def wrapper():
#         """Wrapper function"""
#         return func()
#     return wrapper

# @my_decorator_wrap
# def say_wrap():
#     """Original function"""
#     print("Hi from wrap")

# ============================= practical use cases ==========================
# # Authorization
# def require_admin(func):
#     def wrapper(user):
#         if user == "admin":
#             return func(user)
#         else:
#             print("Access denied!")
#     return wrapper

# @require_admin
# def view_dashboard(user):
#     print(f"{user} is viewing the dashboard")


# # Caching
# cache = {}
# def cached(func):
#     def wrapper(x):
#         if x in cache:
#             print("Returning from cache")
#             return cache[x]
#         result = func(x)
#         cache[x] = result
#         return result
#     return wrapper

# @cached
# def square(n):
#     print("Calculating...")
#     return n * n


# def timing(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         print(f"{func.__name__} took {end-start:.4f} seconds")
#         return result
#     return wrapper

# @timing
# def slow_function():
#     time.sleep(1)
#     print("Done")

