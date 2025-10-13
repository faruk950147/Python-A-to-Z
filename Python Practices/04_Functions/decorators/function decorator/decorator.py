# ============================= Function based decorator ========================
def decorator_func(word): # <-- decorator function takes ONE argument (the function)
    def real_decorator(func): # <-- real actual decorator function takes ONE argument (the function)
        def wrapper(message): # <-- wrapper function takes ONE argument (the function)
            print("Before function call")
            func(word)
            print("After function call")
        return wrapper
    return real_decorator


@decorator_func("Python")  # if we pass argument here, it will be passed to the inner function
def say_hello(name):
    print("Hello", name)

say_hello("World")