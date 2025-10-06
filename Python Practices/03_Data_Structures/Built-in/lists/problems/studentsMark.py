
# list in dictionary
studentsMark = [
    {
        "studentInfo": {
            "id": 1,
            "name": "Faruk",
            "department": "CSE",
            "subject": ["Math", "English", "Programming"]
        }
    }
]
print(f"studentsMark [0]: {studentsMark[0]}")
print(f"studentsMark [0]['studentInfo']: {studentsMark[0]['studentInfo']}")
print(f"studentsMark [0]['studentInfo']['name']: {studentsMark[0]['studentInfo']['name']}")
print(f"studentsMark [0]['studentInfo']['subject']: {studentsMark[0]['studentInfo']['subject']}")
print(f"studentsMark [0]['studentInfo']['subject'][0]: {studentsMark[0]['studentInfo']['subject'][0]}")
print(f"studentsMark [0]['studentInfo']['subject'][1]: {studentsMark[0]['studentInfo']['subject'][1]}")
print(f"studentsMark [0]['studentInfo']['subject'][2]: {studentsMark[0]['studentInfo']['subject'][2]}")

# list in tuple
studentsMark = [
    (1, "Faruk", "CSE", ["Math", "English", "Programming"]),
    (2, "Fahad", "EEE", ["Math", "English", "Programming"]),
]
print(f"studentsMark [0]: {studentsMark[0]}")
print(f"studentsMark [0][0]: {studentsMark[0][0]}")
print(f"studentsMark [0][1]: {studentsMark[0][1]}")
print(f"studentsMark [0][2]: {studentsMark[0][2]}")
print(f"studentsMark [0][3]: {studentsMark[0][3]}")
print(f"studentsMark [0][3][0]: {studentsMark[0][3][0]}")
print(f"studentsMark [0][3][1]: {studentsMark[0][3][1]}")
print(f"studentsMark [0][3][2]: {studentsMark[0][3][2]}")


# list in set
studentsMark = [
    {
        "Faruk",
        "Fahad",
        "Faisal",
    }
]
print(type(studentsMark))
print(type(studentsMark[0]))
print(f"studentsMark [0]: {studentsMark[0]}")