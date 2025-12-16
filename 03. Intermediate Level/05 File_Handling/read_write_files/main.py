# ============================= what is file =============================
# A file is a collection of data stored on a computer or other device.

# ============================= file modes =============================
# 'w' mode means create a new file (overwrite if it already exists)
# 'a' mode means append data at the end of the file
# 'r' mode means read data from the file
# 'x' mode means create a new file (fail if it already exists)
import os

# ============================= write to file =============================
# file = open('data.txt', 'w')
# file.write('Hello, World!')
# file.close()
if os.path.exists('data.txt'):
    print("File already exists.")
else:
    with open('data.txt', 'w') as file:
        file.write('Hello, World!')
    print("File created successfully!")

# ============================= read from file =============================
if os.path.exists('data.txt'):
    with open('data.txt', 'r') as file:
        print(file.read())
else:
    print("File does not exist")

# ============================= append to file =============================
if os.path.exists('data.txt'):
    with open('data.txt', 'a') as file:
        file.write('\nHello, World!')
    print("Appended successfully!")
else:
    print("File does not exist")



