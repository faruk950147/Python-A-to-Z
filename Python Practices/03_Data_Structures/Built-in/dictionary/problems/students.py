students = {}
# num = int(input("How many students: "))
# while len(students) < num:
#     roll = int(input(f"Enter roll of student {i+1}: ")) 
#     marks = float(input(f"Enter marks of student roll {roll}: "))
#     if roll not in students:
#         students[roll] = marks
#     else:
#         print("Roll already exists.")
#         continue
# print(f"All students marks: {students}")

students = {}

num = int(input("How many students: "))

for i in range(num):
    roll, marks = input(f"Enter roll and marks of student {i+1}: ").split()
    roll = int(roll)
    marks = float(marks)

    if roll not in students:
        students[roll] = marks
    else:
        print("Roll already exists.")
        continue

print(f"All students marks: {students}")
