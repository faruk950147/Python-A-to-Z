import os
try:
    if os.path.exists("data.txt"):
        data = input("Enter your name: ")
        with open("data.txt", "w+") as file:
            file.write(data)
            file.seek(0)
            print(file.read())
    else:
        print("File does not exist")
except Exception as e:
    print("An error occurred", str(e))


