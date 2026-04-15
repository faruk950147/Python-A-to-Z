
# Python Decorator হলো এমন একটা feature যা দিয়ে তুমি কোনো function-এর behavior modify করতে পারো — function-এর code না বদলিয়েই 🔥

# সহজভাবে:
# Function-এর উপর extra feature add করা

# Basic Concept

# Python-এ function-কে argument হিসেবে pass করা যায় — এই concept দিয়েই decorator কাজ করে।

# 1. Simple Decorator
def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

# Output:
# Before function
# Hello!
# After function

# @my_decorator মানে:

# say_hello = my_decorator(say_hello)
# 2. Arguments সহ Decorator
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs)
        print("After")
        return result
    return wrapper

@my_decorator
def add(a, b):
    return a + b

print(add(5, 3))
# 3. Decorator with Parameter
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def hello():
    print("Hello")

hello()
# 4. Multiple Decorators
def decor1(func):
    def wrapper():
        print("Decor1")
        func()
    return wrapper

def decor2(func):
    def wrapper():
        print("Decor2")
        func()
    return wrapper

@decor1
@decor2
def test():
    print("Function")

test()

# Execution order:
# Decor1
# Decor2
# Function
# Real Life Use Cases
# 1. Login Required (Django style idea)
def login_required(func):
    def wrapper(user):
        if not user:
            print("Login first")
        else:
            func(user)
    return wrapper
# 2. Timing Decorator
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print("Time:", end - start)
    return wrapper
# Summary
# Function কে wrap করে extra behavior add করে
# @decorator_name দিয়ে ব্যবহার করা হয়
# *args, **kwargs দিলে সব ধরনের argument handle করা যায়
# Real project-এ খুব important (auth, logging, caching)


# Python decorator-এ কতগুলো arguments দেওয়া যায়—এর উত্তর হলো: যত খুশি দেওয়া যায়
# কিন্তু সেটা depend করে decorator কীভাবে define করা হয়েছে তার উপর।

# চল একটু সহজভাবে বুঝি 

# 1. No argument decorator

# এখানে decorator কোনো argument নেয় না

def my_decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

@my_decorator
def say_hi():
    print("Hi")

say_hi()
# 2. Function arguments (multiple allowed)

# decorated function যতগুলো argument নেয়, wrapper-এ ততগুলো নিতে পারো

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs)
        print("After")
        return result
    return wrapper

@my_decorator
def add(a, b, c):
    return a + b + c

print(add(1, 2, 3))

# এখানে *args, **kwargs use করলে unlimited arguments handle করা যায়

# 3. Decorator with arguments

# Decorator নিজেই argument নিতে পারে

def repeat(n):   # decorator argument
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def hello():
    print("Hello")

hello()

# এখানে decorator 1টা argument নিচ্ছে (n), কিন্তু তুমি চাইলে multiple দিতে পারো
# 4. Multiple decorator arguments
def custom(msg, times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(times):
                print(msg)
                func(*args, **kwargs)
        return wrapper
    return decorator

@custom("Hi", 2)
def test():
    print("Function called")

test()
# Summary
# Fixed limit নেই
# *args, **kwargs দিলে unlimited arguments
# decorator নিজেও multiple arguments নিতে পারে