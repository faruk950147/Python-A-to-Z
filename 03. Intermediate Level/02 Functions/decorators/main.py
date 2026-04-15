
# Python Decorator হলো এমন একটা feature যা দিয়ে তুমি কোনো function-এর behavior modify করতে পারো — function-এর code না বদলিয়েই 

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

# Python decorator-এর rules (নিয়ম) খুব clearভাবে বুঝে নিলে আর কখনো ভুল হবে না 
# চল সহজভাবে সব important rules দেখি 

# Rule 1: Decorator সবসময় function return করে

# Decorator একটা function নেয় এবং আরেকটা function return করে

def my_decorator(func):
    def wrapper():
        func()
    return wrapper
# Rule 2: @decorator = function replace হয়
@my_decorator
def test():
    pass

# আসলে এটা হয়:

test = my_decorator(test)
# Rule 3: wrapper function দরকার

# Decorator-এর ভিতরে সবসময় wrapper থাকে

def my_decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

# Rule 4: Arguments handle করতে *args, **kwargs ব্যবহার করো
def my_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

# এতে সব ধরনের function handle করা যায়

# Rule 5: Decorator যদি argument নেয় → nested function লাগবে
def my_decorator(arg):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(arg)
            return func(*args, **kwargs)
        return wrapper
    return decorator

# ব্যবহার:

@my_decorator("Hello")
# Rule 6: Execution order (Multiple decorator)
@A
@B
def test():
    pass

# এটা হয়:

test = A(B(test))

# execution:

# A → B → function
# Rule 7: Return value return করতে হবে
def my_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

# না করলে function result হারিয়ে যাবে

# Rule 8: functools.wraps ব্যবহার করা ভালো practice
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

# এতে function name, doc ঠিক থাকে

# Final Shortcut (সব একসাথে)
from functools import wraps

def decorator(arg):
    def real_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print("Decorator arg:", arg)
            return func(*args, **kwargs)
        return wrapper
    return real_decorator
# Summary (1 লাইনে)

# Decorator = function modify করার tool without changing original code   


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

def decorator_with_args(arg1, arg2, arg3):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"Decorator args: {arg1}, {arg2}, {arg3}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@decorator_with_args("Hello", "World", "!")
def greet(name):
    print(f"Hello, {name}")

greet("Alice") 
'''
codeটা একদম perfect এখন আমি step-by-step বুঝিয়ে দিচ্ছি কোন function কী কাজ করছে 

Main Structure
def decorator_with_args(arg1, arg2, arg3):

এটা হলো decorator factory function
মানে: এটা সরাসরি decorator না, বরং decorator তৈরি করে

Step 1: decorator_with_args
def decorator_with_args(arg1, arg2, arg3):

এখানে:

arg1 = "Hello"
arg2 = "World"
arg3 = "!"

যখন তুমি লিখো:

@decorator_with_args("Hello", "World", "!")

তখন এটা run হয়:

decorator = decorator_with_args("Hello", "World", "!") 
Step 2: decorator
def decorator(func):

এটা আসল decorator function

এখানে:

func = greet

মানে:

greet = decorator(greet)
Step 3: wrapper
def wrapper(*args, **kwargs):

এটা function call intercept করে

এখানে:

args = ("Alice",)
Full Flow (Very Important)
যখন Python এইটা দেখে:
@decorator_with_args("Hello", "World", "!")
def greet(name):

এটা internally হয়ে যায়:

greet = decorator_with_args("Hello", "World", "!")(greet)
Execution Time
greet("Alice")

Actually call হয়:

wrapper("Alice")
Inside wrapper
print(f"Decorator args: {arg1}, {arg2}, {arg3}")

Output:

Decorator args: Hello, World, !

তারপর:

return func(*args, **kwargs)

মানে:

greet("Alice")
Final Output
Decorator args: Hello, World, !
Hello, Alice
Short Summary
Function	কাজ
decorator_with_args	decorator তৈরি করে (arguments নেয়)
decorator	function কে wrap করে
wrapper	actual execution control করে

'''

