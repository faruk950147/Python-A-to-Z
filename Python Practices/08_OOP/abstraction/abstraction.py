# ====================== What is Abstraction ======================

# Abstraction is the process of hiding the implementation details of a class and showing only the necessary details to the user. It is a way to reduce the complexity of a program and make it easier to understand and maintain.

from abc import ABC, abstractmethod

# Abstract Class
class Student(ABC):
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Roll: {self.roll}")

    @abstractmethod
    def calculate_result(self):
        """This method must be implemented in child classes"""
        pass


# Concrete Class (inherits from Student)
class CollegeStudent(Student):
    def __init__(self, name, roll, marks):
        super().__init__(name, roll)
        self.marks = marks

    def calculate_result(self):
        avg = sum(self.marks) / len(self.marks)
        if avg >= 40:
            print(f"{self.name} passed with average: {avg:.2f}")
        else:
            print(f"{self.name} failed with average: {avg:.2f}")


# Another subclass
class SchoolStudent(Student):
    def __init__(self, name, roll, grade):
        super().__init__(name, roll)
        self.grade = grade

    def calculate_result(self):
        print(f"{self.name}'s grade is {self.grade}")


# Object 
c1 = CollegeStudent("Faruk Ahmed", 101, [80, 75, 90])
c1.show_details()
c1.calculate_result()

print("--------------")

s1 = SchoolStudent("Rafi", 55, "A+")
s1.show_details()
s1.calculate_result()
