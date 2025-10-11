# ===================== what is annotation =====================
# annotation is a feature in python that allows you to specify the type of a variable,
# function parameter, or return value class or function
# it is not mandatory but it is a good practice to use it
# runtime it will not check the type of the variable,
# function parameter, or return value

# ===================== annotation for variable =====================
# annotation for variable is a feature in python that allows you to specify the type of a variable

x: int = 10
y: str = "10"
z: float = 10.0

print(x)
print(y)
print(z)

# ===================== annotation for function =====================
# annotation for function is a feature in python that allows you to specify the type of a function

def add(a: int, b: int) -> int:
    return a + b

print(add(1, 2))

# ===================== annotation for class =====================
# annotation for class is a feature in python that allows you to specify the type of a class

class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"Person(name={self.name}, age={self.age})"

    def __repr__(self) -> str:
        return f"Person(name={self.name}, age={self.age})"
    

person = Person("John", 30)
print(person)
print(repr(person))

# ===================== annotation for list =====================
# annotation for list is a feature in python that allows you to specify the type of a list

x: list[int] = [1, 2, 3, 4, 5]
print(x)

# ===================== annotation for tuple =====================
# annotation for tuple is a feature in python that allows you to specify the type of a tuple

x: tuple[int, int, int] = (1, 2, 3)
print(x)

# ===================== annotation for set =====================
# annotation for set is a feature in python that allows you to specify the type of a set

x: set[int] = {1, 2, 3}
print(x)

# ===================== annotation for dictionary =====================
# annotation for dictionary is a feature in python that allows you to specify the type of a dictionary

x: dict[str, int] = {"a": 1, "b": 2, "c": 3}
print(x)

# ===================== annotation for function =====================
# annotation for function is a feature in python that allows you to specify the type of a function

def add(a: int, b: int) -> int:
    return a + b

print(add(1, 2))