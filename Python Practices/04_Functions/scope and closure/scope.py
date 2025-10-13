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
    # return inner_func() # here inner_func() is called
    return inner_func # here inner_func is returned

my_func = outer_func()
my_func()
