def decorator(func):
    def wrapper():
        print("Start")
        func()
        print("End")
    return wrapper

@decorator
def say_hello():
    print("Hello")
    
say_hello()