class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        # it's not a property so it will not update when grade is updated
        # self.message = self.name + " " + "got grade " + self.grade 

    @property
    def message(self):
        # it's a property so it will update when grade is updated
        return self.name + " " + "got grade " + self.grade



if __name__ == "__main__":
    student = Student("John", 20, "A+")
    student.grade = "B" 
    print(student.name)
    print(student.age)
    print(student.grade)
    print(student.message)
    