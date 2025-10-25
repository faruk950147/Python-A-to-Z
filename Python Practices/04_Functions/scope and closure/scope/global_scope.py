# =============================== what is global scope ===============================
# global scope is the scope of a variable or identifier that is defined inside a global namespace.

# =============================== example ===============================
x = 10

def func():
    print(x)

func()

# =============================== accessing global scope ===============================
def func():
    # when we want to access a global scope inside a function,
    # we use the global keyword.change the global scope inside a function, 
    # that's why we use the global keyword before the variable.
    # change the value of global scope inside a function,
    global x 
    x = 20
    print(x)

func()

print(globals())
