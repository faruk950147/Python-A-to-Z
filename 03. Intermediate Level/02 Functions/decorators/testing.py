# decorator implementation
def my_decorator(func):
    def wrapper():
        print("Before function")
        if True:
            func()
        print("After function")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
