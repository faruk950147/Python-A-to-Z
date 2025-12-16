
# ============================= 1. Function as Argument =======================================

# def display(func):
#     print(func(2,3))
    
# def add(x, y):
#     return x + y

# def mul(x, y):
#     return x * y

# display(add)
# display(mul)

# ============================= 2. Function as Return =======================================
def display():
    def add(x, y):
        return x + y
    return add

add = display()
print(add(2, 3))


# ============================= 3. Function Higher Order =======================================

def display(func, nums):
    return func(nums)

def add(nums):
    return sum(nums)

add = display(add, [2, 3, 4])
print(add)
