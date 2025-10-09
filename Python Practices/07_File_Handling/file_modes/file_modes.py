# ===================== what is file modes =====================
# File modes are used to specify the type of access you want to have on a file.
# Here are the most common file modes:
# 'r' - Read mode (default)
# 'w' - Write mode (create a new file or overwrite an existing file)
# 'a' - Append mode (append to the end of the file)
# 'x' - Create mode (create a new file, error if it already exists)
# 'b' - Binary mode (for binary files)
# 't' - Text mode (default)
import os
# ============================= CREATE & WRITE CSV FILE =============================
with open('example.txt', 'w') as file:
    file.write('Hello, World!')

print("example.txt file created and written successfully!")

# ============================= APPEND TO CSV FILE =============================
with open('example.txt', 'a') as file:
    file.write('\nHello, World!')

print("example.txt file appended successfully!")

# ============================= READ CSV FILE =============================
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

print("example.txt file read successfully!")

# ============================= DELETE CSV FILE =============================

os.remove('example.txt')

print("example.txt file deleted successfully!")

# ============================= file functions =============================
# open() function is used to open a file.
# close() function is used to close a file.
# read() function is used to read a file.
# write() function is used to write a file.
# append() function is used to append to a file.
# remove() function is used to remove a file.
# rename() function is used to rename a file.
# mkdir() function is used to create a directory.
# rmdir() function is used to remove a directory.
# listdir() function is used to list the contents of a directory.
# chdir() function is used to change the current working directory.
# getcwd() function is used to get the current working directory.
# mkdir() function is used to create a directory.
# rmdir() function is used to remove a directory.
# listdir() function is used to list the contents of a directory.
# chdir() function is used to change the current working directory.
# getcwd() function is used to get the current working directory.
# readline() function is used to read a line from a file.
# readlines() function is used to read all lines from a file.
# seek() function is used to change the file cursor position.
# tell() function is used to get the file cursor position.
# flush() function is used to flush the file buffer.
# isatty() function is used to check if the file is a terminal.
# is_open() function is used to check if the file is open.

# ============================= read file =============================
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

print("example.txt file read successfully!")

# ============================= delete file =============================
os.remove('example.txt')

print("example.txt file deleted successfully!")

# ============================= append to file =============================
with open('example.txt', 'a') as file:
    file.write('\nHello, World!')

print("example.txt file appended successfully!")

# ============================= write to file =============================
with open('example.txt', 'w') as file:
    file.write('Hello, World!')

print("example.txt file written successfully!")

# ============================= create file =============================
with open('example.txt', 'x') as file:
    file.write('Hello, World!')

print("example.txt file created successfully!")

# ============================= binary file =============================
with open('example.txt', 'b') as file:
    file.write('Hello, World!')

print("example.txt file written successfully!")

# ============================= text file =============================
with open('example.txt', 't') as file:
    file.write('Hello, World!')

print("example.txt file written successfully!")

# ============================= rename file =============================
os.rename('example.txt', 'example2.txt')

print("example.txt file renamed successfully!")

# ============================= create directory =============================
os.mkdir('example_dir')

print("example_dir directory created successfully!")

# ============================= remove directory =============================
os.rmdir('example_dir')

print("example_dir directory removed successfully!")

# ============================= list directory =============================
os.listdir('example_dir')

print("example_dir directory listed successfully!")



