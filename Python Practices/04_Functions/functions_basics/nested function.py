# ============================= What is nested function ==============================

# def outer():
#     print("outer")
#     def inner():
#         print("inner")
#     inner()
# outer()

# fun = outer
# fun()

def add(a, b):
    def subtruct(a, b):
        return a - b
    # print(subtruct(9,6))
    return a + b
print(add(9,6))
d = add
print(d(9,7))