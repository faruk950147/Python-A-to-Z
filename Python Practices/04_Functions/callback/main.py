def printName(name, callback):
    print(f"My Name is {name}")
    callback()
    
def printAge(age):
    print(f"My age is {age}")
    
printName('Faruk',  printAge)
