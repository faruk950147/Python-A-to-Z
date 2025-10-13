# ============================= Simple logging decorator =======================

def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}()")
        return func(*args, **kwargs)
    return wrapper

@log_decorator
def add1(a, b):
    return a + b

print("Result:", add1(3, 2))

@log_decorator
def add2(num):
    # total = 0
    # for i in range(len(num)):
    #     total += num[i]
    # return total
    return sum(num)

print("Result:", add2([1, 2, 3, 4, 5]))
