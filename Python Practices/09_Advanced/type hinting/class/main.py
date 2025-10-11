# ===================== what is type hinting =====================
# type hinting is a feature in python that allows you to specify the type of a variable,
# function parameter, or return value class or function
# it is not mandatory but it is a good practice to use it
# runtime it will not check the type of the variable,
# function parameter, or return value   

# ===================== type hinting for class =====================
# type hinting for class is a feature in python that allows you to specify the type of a variable,
# function parameter, or return value class or function

class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"Person(name={self.name}, age={self.age})"

    def __repr__(self) -> str:
        return f"Person(name={self.name}, age={self.age})"