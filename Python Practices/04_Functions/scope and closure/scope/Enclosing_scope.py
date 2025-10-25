# =============================== what is enclosing scope ===============================
# enclosing scope is the scope of a variable or identifier that is defined inside a nested function.

# =============================== example ===============================
def outer_func(x):
    # x is a local scope. but it is accessible inside the nested function.
    def inner_func(y):
        # here x is a enclosing scope.
        # y is a local scope.
        print(x)
        print(y)
    inner_func(20)
outer_func(10)

# =============================== accessing enclosing scope ===============================
def outer_func(x):
    # x is a local scope. but it is accessible inside the nested function.
    def inner_func(y):
        # here x is a enclosing scope.
        # y is a local scope.
        print(x)
        print(y)
    inner_func(20)
outer_func(10)


