with open("data.txt", "r") as file:
    print(file.readable())
    
    

with open("data.txt", "w") as file:
    print(file.writable())