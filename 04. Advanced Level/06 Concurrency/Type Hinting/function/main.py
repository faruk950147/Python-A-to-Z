# ===================== what is type hinting =====================
# type hinting is a feature in python that allows you to specify the type of a variable,
# function parameter, or return value class or function
# it is not mandatory but it is a good practice to use it
# runtime it will not check the type of the variable,
# function parameter, or return value   

# ===================== type hinting for class =====================
# type hinting for class is a feature in python that allows you to specify the type of a variable,
# function parameter, or return value class or function

def add(a: int, b: int) -> int:
    return a + b

print(add(1, 2))
