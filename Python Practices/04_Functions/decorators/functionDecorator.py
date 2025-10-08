# import time
# ============================= What is decorator ==============================
# decorator is a function that takes another function as an argument,
# adds some functionality, and returns a new function. 
# It is used to modify the behavior of a function or class.

# def decorator(func):
#     def wrapper():
#         print("Before function call")
#         func()
#         print("After function call")
#     return wrapper


# # ============================= Function based decorator ==============================
def my_decorator(func):
    def wrapper():
        print("Start")
        func()
        print("End")
    return wrapper

@my_decorator
def say_hello():
    print("Hello")
    
say_hello()


# ============================= function as argument =========================
def greet(func):
    func()

def hello():
    print("Hello World")

greet(hello)


# ============================= function return function =====================
# def outer():
#     def inner():
#         print("I am inner function")
#     return inner

# f = outer()
# # f()


# ============================= @decorator syntax ============================
# @my_decorator
# def say_hi():
#     print("Hi")


# ============================= multiple decorators ==========================
# def deco1(func):
#     def wrapper():
#         print("Deco1 Start")
#         func()
#         print("Deco1 End")
#     return wrapper

# def deco2(func):
#     def wrapper():
#         print("Deco2 Start")
#         func()
#         print("Deco2 End")
#     return wrapper

# @deco1
# @deco2
# def test():
#     print("Function Body")


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


# ============================= class-based decorator ========================
# class MyDecorator:
#     def __init__(self, func):
#         self.func = func
    
#     def __call__(self):
#         print("Before call")
#         self.func()
#         print("After call")

# @MyDecorator
# def greet_class():
#     print("Hello from function")


# ============================= practical use cases ==========================
# # Logging
# def log(func):
#     def wrapper(*args, **kwargs):
#         print(f"Calling {func.__name__}")
#         return func(*args, **kwargs)
#     return wrapper

# @log
# def add(a, b):
#     return a + b


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


# ============================= Test Calls ==============================
# if __name__ == "__main__":
#     say_hello()
#     greet(hello)
#     f()
#     say_hi()
#     test()
#     hello_repeat()
#     print(say_wrap.__name__, "-", say_wrap.__doc__)
#     greet_class()
#     print(add(5, 10))
#     view_dashboard("admin")
#     view_dashboard("guest")
#     print(square(4))
#     print(square(4))  # Cached
#     slow_function()
