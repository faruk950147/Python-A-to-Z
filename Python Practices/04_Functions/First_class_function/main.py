def outer_func(a):
    def inner_func(b):
        return a + b
    return inner_func  # returning function itself, not calling it

result = outer_func(10) # 10 is a
print(result(20))  # 20 is b, calling inner function