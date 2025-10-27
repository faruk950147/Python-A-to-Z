# ============================= what is file =============================
# A file is a collection of data stored on a computer or other device.

# ============================= file modes =============================
# 'w' mode means create a new file (overwrite if it already exists)
# 'a' mode means append data at the end of the file
# 'r' mode means read data from the file
# 'x' mode means create a new file (fail if it already exists)

# ============================= write to file =============================
# file = open('data.txt', 'w')
# file.write('Hello, World!')
# file.close()

with open('data.txt', 'w') as file:
    file.write('Hello, World!')

# ============================= read from file =============================
with open('data.txt', 'r') as file:
    print(file.read())

# ============================= append to file =============================
with open('data.txt', 'a') as file:
    file.write('\nHello, World!')




