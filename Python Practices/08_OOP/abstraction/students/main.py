# Custom abstract-like base class
class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def show_info(self):
        print(f"Name: {self.name}, Roll: {self.roll}")

    def calculate_result(self):
        # Abstract-like enforcement
        raise NotImplementedError("You must implement 'calculate_result()' in subclass.")


# Subclass 1
class CollegeStudent(Student):
    def __init__(self, name, roll, marks):
        super().__init__(name, roll)
        self.marks = marks

    def calculate_result(self):
        avg = sum(self.marks) / len(self.marks)
        if avg >= 40:
            print(f"{self.name} Passed (Average: {avg:.2f})")
        else:
            print(f"{self.name} Failed (Average: {avg:.2f})")


# Subclass 2
class SchoolStudent(Student):
    def __init__(self, name, roll, grade):
        super().__init__(name, roll)
        self.grade = grade

    def calculate_result(self):
        print(f"{self.name}'s Grade: {self.grade}")


# Working Example
c = CollegeStudent("Faruk Ahmed", 101, [85, 78, 90])
c.show_info()
c.calculate_result()

print("--------------")

s = SchoolStudent("Rafi", 202, "A+")
s.show_info()
s.calculate_result()


# Example (Error: Not Implemented)
# obj = Student("Tuhin", 303)
# obj.calculate_result()  # This will raise NotImplementedError