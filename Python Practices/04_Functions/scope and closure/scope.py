# ======================= what is scope =======================

# Scope is the region of the code where a variable is accessible.

# There are 4 types of scope:
# 1. Local scope
# 2. Enclosing scope
# 3. Global scope
# 4. Built-in scope

# Local scope: The variables defined inside a function are only accessible inside that function.
# Enclosing scope: The variables defined inside a function are only accessible inside that function.
# Global scope: The variables defined inside a function are only accessible inside that function.
# Built-in scope: The variables defined inside a function are only accessible inside that function.

def outer_func():
    x = 'local'
    def inner_func():
        print(x)
    return inner_func() # here inner_func() is called
    # return inner_func # here inner_func is returned

a = outer_func()
print(a)

def outer_func():
    x = 5
    def inner_func():
        y = 6
        return x + y
    return inner_func # here inner_func is returned

a = outer_func()
print(a())