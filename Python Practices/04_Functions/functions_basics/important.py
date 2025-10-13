# ============================= nested function return call =============================
# def outer_func():
#     x = 'local'
#     def inner_func():
#         print(x)
#     return inner_func() # here inner_func() is called

# outer_func()

# ============================= nested function return reference =============================
def outer_func():
    x = 'local'
    def inner_func():
        print(x)
    return inner_func # here inner_func is returned

outer_func()

