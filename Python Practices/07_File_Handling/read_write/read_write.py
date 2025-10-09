# ======================== read write ========================
file = open('example.txt', 'r')
file.write('Hello, World!')
file.close()


# ======================== read ========================
with open('example.txt', 'r') as file:
    print(file.read())
    
    
    