# list in dictionary
studentsMark = [
    {
        "id": 1,
        "name": "Faruk",
        "department": "CSE",
        "subject": ["Math", "English", "Programming"]
    }
]
print(type(studentsMark))
print(f"type(studentsMark[0]) dict: {type(studentsMark[0])}")
print(f"studentsMark [0]: {studentsMark[0]}")
print(f"studentsMark [0]['id']: {studentsMark[0]['id']}")
print(f"studentsMark [0]['name']: {studentsMark[0]['name']}")
print(f"studentsMark [0]['department']: {studentsMark[0]['department']}")
print(f"studentsMark [0]['subject']: {studentsMark[0]['subject']}")
print(f"studentsMark [0]['subject'][0]: {studentsMark[0]['subject'][0]}")
print(f"studentsMark [0]['subject'][1]: {studentsMark[0]['subject'][1]}")
print(f"studentsMark [0]['subject'][2]: {studentsMark[0]['subject'][2]}")


# list in set
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
print(type(studentsMark))
print(f"type(studentsMark[0]) dict: {type(studentsMark[0])}")
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
print(f"type(studentsMark[0]) set: {type(studentsMark[0])}")
print(f"studentsMark [0]: {studentsMark[0]}")