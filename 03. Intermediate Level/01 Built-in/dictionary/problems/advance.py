students = {}

while True:
    data = input("Enter roll number and marks: ").split()

    if len(data) != 2:
        print("Please enter exactly 2 values (roll marks).")
        continue

    roll_input, marks_input = data

    if not roll_input.isdigit():
        print("Roll must be an integer.")
        continue

    try:
        roll = int(roll_input)
        marks = float(marks_input)
    except:
        print("Marks must be a number.")
        continue

    if roll in students:
        print("Roll already exists. Try a different roll.")
        continue

    students[roll] = marks

    choice = input("Do you want to add more students? (y/n): ").strip().lower()

    if choice == 'n':
        print("Program exited successfully.")
        break
    elif choice != 'y':
        print("Invalid choice. Please enter y or n.")


print("\nStudent List:")
for roll, marks in students.items():
    print(f"Roll: {roll}, Marks: {marks}")     
