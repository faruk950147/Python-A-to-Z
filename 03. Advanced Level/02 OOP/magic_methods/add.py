# print(9 + 9)
# print(int.__add__(9, 9))
# print((9).__add__(9))

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __add__(self, other):
        return self.age + other.age
    def __str__(self):
        return f"{self.name} is {self.age} years old"
if __name__ == "__main__":
    student1 = Student("John", 20)
    student2 = Student("Jane", 21)
    print(student1 + student2)
    print(student1)

