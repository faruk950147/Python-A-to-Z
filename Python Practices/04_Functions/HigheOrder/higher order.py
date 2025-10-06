# ============================= What is Higher-Order Function ==============================
# A higher-order function is a function that:
# - Takes one or more functions as arguments
# - OR returns another function as a result

# ============================= 1. Function as Argument (pass) =======================================
def higher_order(func, a, b):   # takes function + args
    return func(a, b)           # calls the function

def add(x, y):
    return x + y

def mul(x, y):
    return x * y

print(higher_order(add, 10, 20))   # 30
print(higher_order(mul, 5, 6))     # 30


# ============================= 2. Function Return =======================================
def higher_order(op):     # takes a string
    def add(x, y):
        return x + y

    def mul(x, y):
        return x * y

    if op == "add":
        return add        # returning function (not calling)
    else:
        return mul
    
# ============================= 3. Function as another function =======================================

# Getting functions
f1 = higher_order("add")   # f1 = add
f2 = higher_order("mul")   # f2 = mul

print(f1(10, 20))   # 30
print(f2(5, 6))     # 30


def higher_order(func):   # here it takes another function as an argument
    print("Inside HOF")
    func()   # here it calls the function

def say_hello():
    print("Hello!")

higher_order(say_hello)
# Example: passing a function into another function

# Example: higher-order function
def higher_order_function(a, b, callback):
    return callback(a, b)

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

print(higher_order_function(10, 20, add))

def doTask(task, callback):
    print("Doing task:", task)
    callback()

def done():
    print("Task finished!")

doTask("Learning JS", done)

# ============================= function returning function ================================
# Example: a function that creates and returns another function

# ============================= built-in higher-order functions ============================
# map(), filter(), reduce(), sorted(), any(), all()

# ============================= custom higher-order function ===============================
# Writing your own higher-order functions

# ============================= higher-order + lambda ======================================
# Using lambda expressions inside higher-order functions

# ============================= relation with decorators ===================================
# Decorators are implemented using higher-order functions

# ============================= practical use cases ========================================
# - Callbacks
# - Functional programming
# - Event handling
# - Wrapping/reusing logic
