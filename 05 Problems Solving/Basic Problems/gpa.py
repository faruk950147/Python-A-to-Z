
# Grade Point Average
marks = {
    "Programming": 3.37,
    "Data Structure": 3.37,
    "Database": 3.37,
    "Web Development": 3.37,
    "Software Engineering": 3.61,
    "Computer Network": 3.50,
}

total = sum(marks.values())
print("Total GPA:", round(total/len(marks), 2))