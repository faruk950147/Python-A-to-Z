# Cumulative Grade Point Average
marks = {
    "1st Semester": 3.37,
    "2nd Semester": 3.37,
    "3rd Semester": 3.37,
    "4th Semester": 3.37,
    "5th Semester": 3.61,
    "6th Semester": 3.50,
    "7th Semester": 3.45,
    "8th Semester": 4.00,
}

total = sum(marks.values())

cgpa = total / len(marks)
if cgpa >= 3.75:
    print("Excellent")
elif cgpa >= 3.5:
    print("Good")
elif cgpa >= 3.0:
    print("Average")
else:
    print("Below Average")