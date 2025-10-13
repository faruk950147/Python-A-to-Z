# ============================= Decorator with arguments =======================
def decorator_func(word): # <-- decorator function takes ONE argument (the function)
    def real_decorator(func): # <-- real actual decorator function takes ONE argument (the function)
        def wrapper(message): # <-- wrapper function takes ONE argument (the function)
            print("Before function call")
            func(message)
            print("After function call")
        return wrapper
    return real_decorator

@decorator_func("Python")
def say_hello_arg(name):
    print("Hello", name)

say_hello_arg("World")


# ============================= Decorator with *args and **kwargs ================
# def decorator_args(func): # <-- decorator function takes ONE argument (the function)
#     def wrapper(*args, **kwargs): # <-- real actual wrapper function takes ONE argument (the function)
#         print("Before function call")
#         func(*args, **kwargs)
#         print("After function call")
#     return wrapper

# @decorator_args
# def say_hello_args(name, age):
#     print(f"Hello {name}, you are {age} years old.")

# say_hello_args("John", 30)