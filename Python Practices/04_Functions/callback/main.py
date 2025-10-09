
def printName(name, callback):
    print(f"My Name is {name}")
    callback(21)   # here callback function is age and 21 is the argument

def printAge(age):
    print(f"My age is {age}")

printName('Faruk', printAge)
