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

# ============================== write file ===========================
with open('data.txt', 'w') as file:
    file.write('Hello, World!')

# ============================= read file =============================
with open('data.txt', 'r') as file:
    content = file.read()
    print(content)

print("data.txt file read successfully!")

# ============================= append to file =============================
with open('data.txt', 'a') as file:
    file.write('\nHello again!')

print("data.txt file appended successfully!")

# ============================= binary file =============================
with open('data.txt', 'wb') as file:
    file.write(b'Hello in binary!')

print("data.txt binary written successfully!")

# ============================= rename file =============================
os.rename('data.txt', 'data2.txt')
print("data.txt file renamed successfully!")

# ============================= create directory =============================
os.mkdir('data_dir')
print("data_dir directory created successfully!")

# ============================= list directory =============================
print(os.listdir('.'))
print("Current directory listed successfully!")

# ============================= remove directory =============================
os.rmdir('data_dir')
print("data_dir directory removed successfully!")

# ============================= delete file =============================
os.remove('data2.txt')
print("data2.txt file deleted successfully!")
