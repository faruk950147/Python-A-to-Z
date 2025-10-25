# =============================== what is local scope ===============================
# local scope is the scope of a variable or identifier that is defined inside a function.
# and parameters are also local scope.


# =============================== example ===============================
def my_func():
    x = 10
    print(x)
    print(locals()) # {'x': 10}

my_func()

# =============================== accessing local scope ===============================
def my_func():
    # local scope it is not accessible outside the function 
    x = 10
    y = 20
    z = 30
    print(x)
    print(locals()) # {'x': 10, 'y': 20, 'z': 30}

my_func()
# NameError: name 'x' is not defined because it is not accessible outside the function
# print(x) 

# =============================== local scope in nested functions ===============================
# local scope in nested functions is the scope of a variable or identifier that is defined inside a nested function.
# and parameters are also local scope.
def outer_func(x):
    def inner_func(y):
        print(x)
        print(y)
    inner_func(20)
outer_func(10)
