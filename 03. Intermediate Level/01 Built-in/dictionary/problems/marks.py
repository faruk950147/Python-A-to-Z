# studentsMarks = {
#     "faruk": {
#         "details":
#             {
#                 "roll": 101, "dept": "CSE", "marks": {"C": 85, "C++": 80, "Python": 85, "DS": 90, "DBMS": 88, "OS": 92, "CN": 95}
#             }
#         },
#     "tom": {
#         "details":
#             {
#                 "roll": 102, "dept": "CSE", "marks": {"C": 85, "C++": 80, "Python": 85, "DS": 90, "DBMS": 88, "OS": 92, "CN": 95}
#             }
#         },
#     "jerry": {
#         "details":
#             {
#                 "roll": 103, "dept": "CSE", "marks": {"C": 85, "C++": 80, "Python": 85, "DS": 90, "DBMS": 88, "OS": 92, "CN": 95}
#             }
#         }
# }
# for student in studentsMarks:
#     # printed the name of the student
#     # print(student)
#     # printed the details of the student
#     # print(studentsMarks[student])
#     # printed the marks of the student
#     length = len(studentsMarks[student]["details"]["marks"])
#     percentage = sum(studentsMarks[student]["details"]["marks"].values()) / length
#     print(f"{student} : {percentage:.2f} %")
''' 
def calculate_percentages(students):
    for student in students:
        marks = students[student]["details"]["marks"]
        length = len(marks)
        percentage = sum(marks.values()) / length
        print(f"{student} : {percentage:.2f} %")

studentsMarks = {
    "faruk": {"details": {"roll": 101, "dept": "CSE", "marks": {"C": 85, "C++": 80, "Python": 85, "DS": 90, "DBMS": 88, "OS": 92, "CN": 95}}}, 
    "tom": {"details": {"roll": 102, "dept": "CSE", "marks": {"C": 85, "C++": 80, "Python": 85, "DS": 90, "DBMS": 88, "OS": 92, "CN": 95}}}, 
    "jerry": {"details": {"roll": 103, "dept": "CSE", "marks": {"C": 85, "C++": 80, "Python": 85, "DS": 90, "DBMS": 88, "OS": 92, "CN": 95}}}
}

calculate_percentages(studentsMarks)


class Student:
    def __init__(self, name, details):
        self.name = name
        self.details = details

    def percentage(self):
        marks = self.details["marks"]
        return sum(marks.values()) / len(marks)

studentsMarks = {
    "faruk": {"details": {"roll": 101, "dept": "CSE", "marks": {"C": 85, "C++": 80, "Python": 85, "DS": 90, "DBMS": 88, "OS": 92, "CN": 95}}}, 
    "tom": {"details": {"roll": 102, "dept": "CSE", "marks": {"C": 85, "C++": 80, "Python": 85, "DS": 90, "DBMS": 88, "OS": 92, "CN": 95}}}, 
    "jerry": {"details": {"roll": 103, "dept": "CSE", "marks": {"C": 85, "C++": 80, "Python": 85, "DS": 90, "DBMS": 88, "OS": 92, "CN": 95}}}
}

students = [Student(name, data["details"]) for name, data in studentsMarks.items()]

for student in students:
    print(f"{student.name} : {student.percentage():.2f} %")
    
    
'''

