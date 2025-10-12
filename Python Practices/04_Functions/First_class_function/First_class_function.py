# ============================= What is First-Class Function ==============================
# In Python, functions are first-class objects:
# - They can be assigned to variables
# - They can be passed as arguments
# - They can be returned from other functions
# - They can be stored in data structures

# ============================= First-Class Function Uses =============================================
# - Callbacks
# - Decorators
# - Event handling
# - Functional programming patterns

# ============================= First-Class Function Examples =============================================

# 1. You can store a function in a variable
def greet(name):
    return f"Hello, {name}!"

say_hello = greet  # storing function in a variable
print(say_hello("Faruk"))


# 2. You can pass a function as an argument
def call_func(func, value):
    # get function as an argument and value as an argument
    # return function with value as an argument
    # return greet("Ahmed") means return greet function with "Ahmed" as an argument
    return func(value)

print(call_func(greet, "Ahmed"))


# 3. You can return a function from another function
def outer_func():
    def inner_func():
        return "I'm inside the outer function!"
    return inner_func  # returning function itself, not calling it

result = outer_func()
print(result())  # calling inner function


# 4. You can return a function from another function
def outer_func(a):
    def inner_func(b):
        return a + b
    return inner_func  # returning function itself, not calling it

result = outer_func(10)
print(result())  # calling inner function


# 5. You can keep functions inside data structures
def add(x, y): return x + y
def sub(x, y): return x - y
def mul(x, y): return x * y

operations = {
    "add": add,
    "sub": sub,
    "mul": mul
}

print(operations["add"](10, 5))
print(operations["sub"](10, 5))
print(operations["mul"](10, 5))
