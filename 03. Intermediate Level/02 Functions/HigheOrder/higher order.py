# ============================= What is Higher-Order Function ==============================
# A higher-order function is a function that:
# - Takes one or more functions as arguments
# - OR returns another function as a result

# Callback Function

# Callback function হলো এমন একটি function,
# যেটাকে argument হিসেবে অন্য একটি function-এর মধ্যে পাঠানো হয়
# এবং ওই function-এর ভিতরেই call (execute) করা হয়।

# সহজ ভাষায়
# একটি function আরেকটি function-কে বলে দেয়—
# "আমার কাজ শেষ হলে তুমি এই functionটা চালাবে।"


# Higher Order Function

# Higher Order Function হলো এমন একটি function,
# যেটা অন্য একটি function-কে argument হিসেবে নেয়
# অথবা একটি function return করে।

# সহজ ভাষায়
# যে function, function নিয়ে কাজ করে
# সেটাই Higher Order Function।


# Callback Function vs Higher Order Function

# | Callback Function                         | Higher Order Function                          |
# | ----------------------------------------- | ---------------------------------------------- |
# | যেই function-কে argument হিসেবে পাঠানো হয় | যেই function argument হিসেবে অন্য function নেয় |
# | পাঠানো function                           | নেওয়া function                                 |
# | Higher Order function-এর ভিতরে চলে        | Callback function-কে call করে                  |
# | Example: add()                            | Example: calculate()                           |

from functools import reduce

# ============================= 1. Function as Argument =======================================
def higher_order1(func, a, b):   # takes a function and two numbers
    return func(a, b)            # calls the given function with a and b

def add(x, y):
    return x + y

def mul(x, y):
    return x * y

print(higher_order1(add, 10, 20))   # 30
print(higher_order1(mul, 5, 6))     # 30


# ============================= 2. Function Returning Another Function =======================
def higher_order2(op):   # takes a string as operator name
    def add(x, y):
        return x + y

    def mul(x, y):
        return x * y

    if op == "add":
        return add      # returns the 'add' function (not calling it)
    else:
        return mul      # returns the 'mul' function
    
# getting the returned functions
f1 = higher_order2("add")   # f1 now refers to 'add'
f2 = higher_order2("mul")   # f2 now refers to 'mul'

print(f1(10, 20))   # 30
print(f2(5, 6))     # 30


# ============================= 3. Function as Argument =======================================
def higher_order3(func):   # takes another function as argument
    print("Inside HOF")
    func()   # calls the received function

def say_hello():
    print("Hello!")

higher_order3(say_hello)


# ============================= 4. Function as Argument (Higher-Order Function Example) ===================
def higher_order_function(a, b, func):  # takes a callback function
    return func(a, b)

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

print(higher_order_function(10, 20, add))   # 30


# ============================= 5. Higher-Order Function  ================================
def doTask(task, func):   # takes a task description and a callback
    print("Doing task:", task)
    func()                # calls the callback after finishing the task

def done():
    print("Task finished!")

doTask("Learning JS", done)


# ============================= built-in higher-order functions ============================
# map(), filter(), reduce(), sorted(), any(), all()
def square(x):
    return x * x

print(list(map(square, range(1, 6))))

print(list(filter(lambda x: x % 2 == 0, range(1, 6))))

print(reduce(lambda x, y: x + y, range(1, 6)))

print(sorted([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]))

print(any([False, False, True]))

print(all([True, True, True]))

# ============================= custom higher-order function ===============================
# Writing your own higher-order functions
def higher_order_function(func):
    return func()

def say_hello():
    print("Hello!")

print(higher_order_function(say_hello))

# ============================= higher-order + lambda ======================================
# Using lambda expressions inside higher-order functions
print(higher_order_function(lambda: print("Hello!")))

# ============================= relation with decorators ===================================
# Decorators are implemented using higher-order functions
def decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@decorator
def say_hello():
    print("Hello!")

say_hello()

def decorator(func, *args, **kwargs):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        for arg in args:
            print(arg)
        for key, value in kwargs.items():
            print(key, value)
        func(*args, **kwargs)
        print("Something is happening after the function is called.")
    return wrapper

@decorator
def say_hello(name, age):
    print("Hello", name, "you are", age, "years old.")
    
def calculate(func, *args, **kwargs):
    return func(*args, **kwargs)

def add(*args):
    return sum(args)

def sub(*args):
    return args[0] - sum(args[1:])

def mul(*args):
    return args[0] * sum(args[1:])

def div(*args):
    return args[0] / sum(args[1:])

print(calculate(add, 10, 20, 30))
print(calculate(sub, 10, 20, 30))
print(calculate(mul, 10, 20, 30))
print(calculate(div, 10, 20, 30))

# ============================= practical use cases ========================================
# - Callbacks
# - Functional programming
# - Event handling
# - Wrapping/reusing logic
