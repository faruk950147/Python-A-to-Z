# seek() -> change the cursor position
# tell() -> return the cursor position

with open("data.txt", "r") as file:
    print(file.tell())
    file.seek(10)
    print(file.tell())
    print(file.read())
    file.seek(0)
    print(file.read())
    file.seek(10)
    print(file.read())
    file.seek(0)
    print(file.read())
