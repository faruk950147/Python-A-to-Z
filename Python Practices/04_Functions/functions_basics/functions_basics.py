# ============================= What is function ==============================
# A function is a block of reusable code that performs a specific task.

# ============================= basic type of function ==============================
# 1. First-class function
# 2. Pure function
# 3. Higher-order function
# 4. Lambda function
# 5. Generator function
# 6. Decorator function


# 1. First-class function


# 1. First-class function
def square(x):
    return x * x

f = square   # storing function in a variable
print(f(5))  # output: 25

# 1. You can store a function in a variable
def greet(name):
    return f"Hello, {name}!"

say_hello = greet  # storing function in a variable
print(say_hello("Faruk"))


# 2. You can pass a function as an argument
def call_func(func, value):
    return func(value)

print(call_func(greet, "Ahmed"))


# 3. You can return a function from another function
def outer_func():
    def inner_func():
        return "I'm inside the outer function!"
    return inner_func  # returning function itself, not calling it

result = outer_func()
print(result())  # calling inner function


# 4. You can keep functions inside data structures
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


# 2. Pure function
# A pure function is one that:

# Always gives the same output for the same input

# Does not cause side effects (doesn’t modify global state or external variables)

# 2. Pure function
def add(a, b):
    return a + b

print(add(2, 3))  # 5
print(add(2, 3))  # 5 again (same input → same output)


# 3. Impure function (because it changes a global variable)
total = 0
def add_to_total(x):
    global total
    total += x
    return total
print(add_to_total(10))  # output: 10
print(add_to_total(20))  # output: 30

# 4. Higher-order function
# A higher-order function is a function that:

# Takes another function as an argument, OR

# Returns a function as a result

# 5. Function as argument
def apply(func, value):
    return func(value)

print(apply(lambda x: x * 2, 5))  # output: 10

# 5. Function as argument
def apply(callback, value,  value2):
    return callback(value, value2)

def add(x, y):
    return x + y

print(apply(add, 2, 3))  # output: 5

def display(callback, *args):
    callback(*args)

def print_sum(x, y):
    print(x + y)

def print_product(x, y):
    print(x * y)

display(print_sum, 2, 3)  # output: 5
display(print_product, 2, 3)  # output: 6

# 6. Function as return value
def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

times3 = make_multiplier(3)
print(times3(10))  # output: 30

