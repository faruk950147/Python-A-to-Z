class MarkGraded:
    def __init__(self, marks):
        
        # marks = [sub1, sub2, sub3, ..., sub7]
        self.marks = marks  

    # it is a helper method, it takes a mark and returns a grade
    def markGraded(self, mark):
        if mark >= 90:
            return "A"
        elif mark >= 80:
            return "B"
        elif mark >= 70:
            return "C"
        elif mark >= 60:
            return "D"
        else:
            return "F"

    # it returns all grades of the subjects
    def allGrades(self):
        return [self.markGraded(mark) for mark in self.marks]

    # it returns the final grade based on the average of all marks
    def finalGrade(self):
        average = sum(self.marks) / len(self.marks)
        return self.markGraded(average)
    
    # it returns the average of all marks
    def points(self):
        return sum(self.marks) / len(self.marks)
        

if __name__ == "__main__":
    # here is main code
    # marks of 7 subjects
    marks = [95, 85, 78, 88, 92, 67, 74]  
    student = MarkGraded(marks)
    # all individual grades
    print("Individual Grades:", student.allGrades())  
    # final grade
    print("Final Grade:", student.finalGrade())      
    # average
    print("Average:", student.points())
