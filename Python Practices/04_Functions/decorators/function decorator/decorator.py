def decorator_func(word):
    def real_decorator(func):
        def wrapper(message):
            print("Before function call")
            func(word)
            print("After function call")
        return wrapper
    return real_decorator


@decorator_func("Python")  # if we pass argument here, it will be passed to the inner function
def say_hello(name):
    print("Hello", name)

say_hello("World")
