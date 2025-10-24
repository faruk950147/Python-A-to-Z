class MarkGraded:
    def __init__(self, marks):
        self.marks = marks  

    # individual mark to grade & grade point
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

    # all grades and points
    def allGrades(self):
        return [self.markGraded(mark) for mark in self.marks]

    # GPA calculation like real life
    def gpa(self):
        points = [self.markGraded(mark)[1] for mark in self.marks]
        gpa = sum(points) / len(points)
        return round(gpa, 2)  # round to 2 decimal places

    # final grade based on GPA
    def finalGrade(self):
        gpa = self.gpa()
        if gpa >= 5.0:
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

if __name__ == "__main__":
    marks = [95, 85, 78, 88, 92, 67, 74]  
    student = MarkGraded(marks)

    print("Individual Grades & Points:")
    for i, (grade, point) in enumerate(student.allGrades(), 1):
        print(f"Subject {i}: Grade {grade}, Point {point}")

    print("GPA:", student.gpa())
    print("Final Grade:", student.finalGrade())
