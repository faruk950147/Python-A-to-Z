# class and intance annotation is a feature in python that allows you to specify the type of a class and instance
# ===================== 1. instance annotation =====================
from typing import ClassVar, Final, Dict
class A:
    # instance annotation and type alias is str variable
    name: str
    age: int
    gender: str
    # class annotation and type alias is ClassVar[str] variable
    address: ClassVar[str] = "Dhaka"
    # final annotation and type alias is Final[str] variable
    country: Final[str] = "Bangladesh"
    # dict annotation type alias is Dict[str, str] variable
    info: Dict[str, str] = {"name": "John", "age": "30", "gender": "Male"}

a: A = A()
a.name = "John"
a.age = 30
a.gender = "Male"
print(a.name, a.age, a.gender)
print(A.address)
print(A.country)
print(A.info)
# ===================== 2. class annotation =====================
# class annotation is a feature in python that allows you to specify the type of a class
class A:
    def __init__(self, x: int, y: int) -> None:
        self.x: int = x
        self.y: int = y

    def add(self) -> int:
        return self.x + self.y

a: A = A(1, 2)
print(a.add())