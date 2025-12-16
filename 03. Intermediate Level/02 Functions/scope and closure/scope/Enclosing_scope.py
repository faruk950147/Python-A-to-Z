# =============================== What is Enclosing Scope ===============================
# Enclosing scope refers to variables defined in an outer function
# that are accessible inside a nested (inner) function.

# =============================== Example ===============================
def outer_func(x):
    # x is local to outer_func
    def inner_func(y):
        # y is local to inner_func
        # x from outer_func is an enclosing variable here
        print("Enclosing variable x:", x)
        print("Local variable y:", y)
    inner_func(20)

outer_func(10)

# =============================== Accessing and Modifying Enclosing Scope ===============================
def outer_func():
    x = 10  # local to outer_func
    def inner_func():
        nonlocal x  # allows modifying x from outer_func
        x += 5
        print("Modified x inside inner_func:", x)
    inner_func()
    print("x in outer_func after inner_func:", x)

outer_func()
