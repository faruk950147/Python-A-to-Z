studentMark = {
    "name": "Faruk",
    "department": "CSE",
    "subject": {
        "Math": 80,
        "English": 85,
        "Programming": 90
    }
}

print(studentMark)
print(studentMark["name"])
print(studentMark["subject"])
print(studentMark["subject"]["Math"])

# Update
studentMark["subject"]["Programming"] = 95
print(studentMark)

# Add
studentMark["subject"]["Physics"] = 90
print(studentMark)

# Delete
studentMark.pop("subject")
print(studentMark)


# Delete
studentMark.popitem()
print(studentMark)

# dict in list
studentMark = {
    "name": "Faruk",
    "department": "CSE",
    "subject": ['Math', 'English', 'Programming']
}       

print(studentMark)
print(studentMark["name"])
print(studentMark["subject"])
print(studentMark["subject"][0])

# Update
studentMark["subject"][0] = "Physics"
print(studentMark)

# Add
studentMark["subject"].append("Programming")
print(studentMark)

# Delete
studentMark.pop("subject")
print(studentMark)

# Delete
studentMark.popitem()
print(studentMark)

# dict in tuple
studentMark = {
    "name": "Faruk",
    "department": "CSE",
    "subject": ('Math', 'English', 'Programming')
}       

print(studentMark)
print(studentMark["name"])
print(studentMark["subject"])
print(studentMark["subject"][0])

# dict in set
studentMark = {
    "name": "Faruk",
    "department": "CSE",
    "subject": {'Math', 'English', 'Programming'}
}       

print(studentMark)
print(studentMark["name"])
print(studentMark["subject"])