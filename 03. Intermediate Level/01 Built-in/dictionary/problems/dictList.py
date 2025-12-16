# 1. There is a dictionary containing student data. 
# and how fetch the last key-value pair from the dictionary.
students = {
    "name": "Faruk",
    "age": 21,
    "gender": "Male",
    "course": "BSc in CSE",
    "cgpa": 3.5,
    "courses": ["CSE", "EEE", "BBA"]
}
names = list(students.keys())
print(f"{names[-1]}: {students[names[-1]]}")
# print(names[-1]) # access the last key
# print(students[names[-1]]) # access the last value

# 2. write a program to count the number of items having list as value.
students = {
    "name": "Faruk",
    "age": 21,
    "gender": "Male",
    "course": "BSc in CSE",
    "cgpa": 3.5,
    "courses": ["CSE", "EEE", "BBA"],
    "fees": [750000, 1500000, 2500000]
}
count = 0
for value in students.values():
    if isinstance(value, list):
        count += 1
print(count)