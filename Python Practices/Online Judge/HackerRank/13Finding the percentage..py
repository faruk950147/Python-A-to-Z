if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    average = sum(student_marks[query_name]) / len(student_marks[query_name])
    print(f"{average:.2f}")

class Student_Average:
    def __init__(self, n, student_marks, query_name):
        self.n = n
        self.student_marks = student_marks
        self.query_name = query_name

    def get_average(self):
        average = sum(self.student_marks[self.query_name]) / len(self.student_marks[self.query_name])
        return average

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    student = Student_Average(n, student_marks, query_name)
    print(f"{student.get_average():.2f}")