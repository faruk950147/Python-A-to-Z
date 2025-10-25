
# ============================= 1. Function as Argument =======================================

def display(func):
    print(func(2,3))
    
def add(x, y):
    return x + y

def mul(x, y):
    return x * y

display(add)
display(mul)
