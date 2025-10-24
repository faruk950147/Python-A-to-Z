class MarkGraded:
    def __init__(self, marks):
        self.marks = marks  

    # mark to grade & grade point
    def markGraded(self, mark):
        if mark >= 80:
            return "A+", 5.0
        elif mark >= 70:
            return "A", 4.0
        elif mark >= 60:
            return "A-", 3.5
        elif mark >= 50:
            return "B", 3.0
        elif mark >= 40:
            return "C", 2.0
        elif mark >= 33:
            return "D", 1.0
        else:
            return "F", 0.0

    # all grades & points
    def allGrades(self):
        return [self.markGraded(mark) for mark in self.marks]

    # GPA calculation
    def gpa(self):
        points = [self.markGraded(mark)[1] for mark in self.marks]
        if 0.0 in points:  # if any subject fails
            return 0.0
        gpa = sum(points) / len(points)
        return round(gpa, 2)

    # final grade based on GPA
    def finalGrade(self):
        gpa = self.gpa()
        if gpa == 5.0:
            return "A+"
        elif gpa >= 4.0:
            return "A"
        elif gpa >= 3.5:
            return "A-"
        elif gpa >= 3.0:
            return "B"
        elif gpa >= 2.0:
            return "C"
        elif gpa >= 1.0:
            return "D"
        else:
            return "F"

    # print result sheet
    def printResultSheet(self):
        print("Bangladesh Board of Education")
        print("Exam Result Sheet")
        print("-" * 50)
        print(f"{'Subject':<10}{'Number':<10}{'Grade':<10}{'Grade Point':<15}")
        print("-" * 50)
        for i, mark in enumerate(self.marks, 1):
            grade, point = self.markGraded(mark)
            print(f"{i:<10}{mark:<10}{grade:<10}{point:<15}")
        print("-" * 50)
        print(f"GPA: {self.gpa()}")
        print(f"Final Grade: {self.finalGrade()}")
        print("-" * 50)


if __name__ == "__main__":
    marks = [95, 90, 92, 88, 92, 80,80]
    student = MarkGraded(marks)
    student.printResultSheet()
