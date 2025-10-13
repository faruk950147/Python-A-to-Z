# ============================= What is a Decorator ==============================
# A decorator is a function that takes another function as an argument,
# adds or modifies functionality, and returns a new function.
# It allows you to extend or modify the behavior of functions or methods
# without changing their code.

# ============================= Basic Decorator =================================
def decorator2(func): # <-- decorator function takes ONE argument (the function)
    def wrapper(word): # <-- real actual wrapper function takes ONE argument (the function)
        print("Before function call")
        func(word)
        print("After function call")
    return wrapper

@decorator2
def say_hello(word):
    print("Hello", word)

say_hello("World")




# ============================= Multiple decorators ============================
def deco1(func):
    def wrapper():
        print("Deco1 Before")
        func()
        print("Deco1 After")
    return wrapper

def deco2(func):
    def wrapper():
        print("Deco2 Before")
        func()
        print("Deco2 After")
    return wrapper

@deco1
@deco2
def test():
    print("Function Body")

test()
