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
if os.path.exists('data.txt'):
    os.remove('data.txt')
else:
    with open('data.txt', 'w') as file:
        file.write('Hello, World!')

# ============================= read file =============================
if os.path.exists('data.txt'):
    with open('data.txt', 'r') as file:
        content = file.read()
        print(content)
    print("data.txt file read successfully!")
else:
    print("data.txt file does not exist!")

# ============================= append to file =============================
if os.path.exists('data.txt'):
    with open('data.txt', 'a') as file:
        file.write('\nHello again!')
    print("data.txt file appended successfully!")
else:
    print("data.txt file does not exist!")

# ============================= binary file =============================
if os.path.exists('data.txt'):
    with open('data.txt', 'wb') as file:
        file.write(b'Hello in binary!')
    print("data.txt binary written successfully!")
else:
    print("data.txt file does not exist!")

# ============================= rename file =============================
if os.path.exists('data.txt'):
    os.rename('data.txt', 'data2.txt')
    print("data.txt file renamed successfully!")
else:
    print("data.txt file does not exist!")

# ============================= create directory =============================
if os.path.exists('data_dir'):
    os.remove('data_dir')
else:
    os.mkdir('data_dir')
    print("data_dir directory created successfully!")

# ============================= list directory =============================
if os.path.exists('data_dir'):
    print(os.listdir('data_dir'))
    print("data_dir directory listed successfully!")
else:
    print("data_dir directory does not exist!")

# ============================= remove directory =============================
if os.path.exists('data_dir'):
    os.rmdir('data_dir')
    print("data_dir directory removed successfully!")
else:
    print("data_dir directory does not exist!")

# ============================= delete file =============================
if os.path.exists('data2.txt'):
    os.remove('data2.txt')
    print("data2.txt file deleted successfully!")
else:
    print("data2.txt file does not exist!")
