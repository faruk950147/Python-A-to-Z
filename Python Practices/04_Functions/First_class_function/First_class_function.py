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
# Example 1: Function as a Variable
def greet():
    print("Hello from function")
# Assigning function to variable it is first class function 
# what we are doing here is storing function in variable    
greet_var = greet 
print(greet_var)
greet_var()

# Example 2: Function as an Argument
def apply(func, x, y):
    return func(x, y)

def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

result1 = apply(add, 5, 3)  # 8
result2 = apply(multiply, 4, 6)  # 24
print(result1)
print(result2)

# Example 3: Function as a Return Value
def call_func(func):
    func()

def say_hello():
    print("Hello")

call_func(say_hello)   # say_hello function is passed as an argument to call_func function

# Example 4: Function as a Return Value
def outer():
    def inner():
        print("I am inner function")
    return inner

returned_func = outer()
returned_func()

# Example 5: Function as a Return Value
def add(a, b): return a + b
def sub(a, b): return a - b

operations = [add, sub]
print(operations[0](10, 5))  # 15
print(operations[1](10, 5))  # 5

