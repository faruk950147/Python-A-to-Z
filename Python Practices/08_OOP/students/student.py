class Student:
    def __init__(self, name, age, roll, marks):
        self.name = name
        self.age = age
        self.roll = roll
        self.marks = marks

    def result(self):
        if self.marks >= 40:
            return "Pass"
        else:
            return "Fail"

    def grade(self):
        if self.marks >= 80:
            return "A"
        elif self.marks >= 70:
            return "B"
        elif self.marks >= 60:
            return "C"
        elif self.marks >= 50:
            return "D"
        else:
            return "F"

    def percentage(self):
        # let total marks = 300, then percentage = marks / 300 * 100 = (marks / 300) * 100
        return (self.marks / 300) * 100
    
    def average(self):
        # let total marks = 300, then average = marks / 3
        
        return self.marks / 3
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Roll: {self.roll}, Marks: {self.marks}"

if __name__ == "__main__":
    s1 = Student("John", 120, 130, 110)
    s2 = Student("Jane", 120, 230, 210)
    s3 = Student("Jack", 120, 330, 310)
    s4 = Student("Jill", 120, 430, 410)
    s5 = Student("Jim", 120, 530, 510)

    print(s1, "| Result:", s1.result(), "| Grade:", s1.grade(), "| Percentage:", s1.percentage(), "| Average:", s1.average())
    print(s2, "| Result:", s2.result(), "| Grade:", s2.grade(), "| Percentage:", s2.percentage(), "| Average:", s2.average())
    print(s3, "| Result:", s3.result(), "| Grade:", s3.grade(), "| Percentage:", s3.percentage(), "| Average:", s3.average())
    print(s4, "| Result:", s4.result(), "| Grade:", s4.grade(), "| Percentage:", s4.percentage(), "| Average:", s4.average())
    print(s5, "| Result:", s5.result(), "| Grade:", s5.grade(), "| Percentage:", s5.percentage(), "| Average:", s5.average())
