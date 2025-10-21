students = {}

while True:
    try:
        roll, marks = input("Enter roll number and marks: ").split()
        roll = int(roll)
        marks = float(marks)
        if roll not in students:
            students[roll] = marks
        else:
            print("Roll already exists. Please enter a different roll.")
            continue

        choice = input("Do you want to add more students? (y/n): ").strip().lower()
        if choice == 'n':
            print('You have already exit the program.')
            break
        elif choice == 'y':
            continue
        else:
            print('Invalid choice. Please enter y or n.')
            continue
    except Exception as e:
        print(f"Please enter valid integer values (roll marks). Error: {e}")
        continue