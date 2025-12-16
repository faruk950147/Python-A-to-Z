# =============================== What is Local Scope ===============================
# Local scope refers to variables defined inside a function.
# Function parameters are also considered local variables.

# =============================== Example ===============================
def my_func():
    x = 10          # local variable
    print(x)        # can access inside the function
    print(locals()) # shows all local variables: {'x': 10}

my_func()

# =============================== Accessing Local Scope ===============================
def my_func():
    # Local variables are not accessible outside the function
    x = 10
    y = 20
    z = 30
    print(x)        # 10
    print(locals()) # {'x': 10, 'y': 20, 'z': 30}
    
    # Correct way to modify a local variable
    x = 200
    print("Modified x inside function:", x)

my_func()

# print(x)  # NameError: x is not accessible outside the function

# =============================== Local Scope in Nested Functions ===============================
# Variables in nested functions follow local scope rules
# Inner functions can read variables from enclosing functions (outer function variables)
# To modify them, use the 'nonlocal' keyword

def outer_func(x):
    # x is a parameter of outer_func → local to outer_func
    def inner_func(y):
        # y is local to inner_func
        # inner_func can also access variables from the enclosing function
        print("From inner_func, x from outer_func:", x)
        print("From inner_func, y from inner_func:", y)
    inner_func(20)

outer_func(10)
