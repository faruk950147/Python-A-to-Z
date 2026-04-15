class Student:
    def __init__(self, name):
        self.name = name

    def show(self):   # instance method
        print(self.name)

s1 = Student("Faruk")
s1.show()

class Student:
    school = "TMSS"

    @classmethod
    def change_school(cls, name): # class method
        cls.school = name

Student.change_school("ABC School")
print(Student.school)

class Math:
    @staticmethod
    def add(a, b):
        return a + b # static method

print(Math.add(5, 3))