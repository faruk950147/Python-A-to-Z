students = {}

num = int(input("How many students: "))

i = 0
while i < num:
    data = input(f"Enter roll and marks of student {i+1}: ").split()

    if len(data) != 2:
        print("Please enter exactly 2 values (roll marks).")
        continue

    roll_input, marks_input = data

    if not roll_input.isdigit():
        print("Roll must be integer.")
        continue

    roll = int(roll_input)

    try:
        marks = float(marks_input)
    except:
        print("Marks must be a number.")
        continue

    if roll in students:
        print("Roll already exists. Try different roll.")
        continue

    students[roll] = marks
    i += 1   # only valid input হলে count বাড়বে

print("All students marks:", students)
