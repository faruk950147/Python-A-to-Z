# ============================= what is context manager =============================
# Context manager is a way to manage resources.
# It is a way to create a new context manager by using the context manager protocol.
# It is a way to create a new context manager by using the context manager protocol.

# 1. Example
with open("file.txt", "r") as file:
    data = file.read()
    print(data)

# 2. Example
with open("file.txt", "w") as file:
    file.write("Hello, World!")

# 3. Example
with open("file.txt", "a") as file:
    file.write("Hello, World!")

# 4. Example
with open("file.txt", "r+") as file:
    data = file.read()
    print(data)
    file.write("Hello, World!")

# 5. Example
with open("file.txt", "x") as file:
    file.write("Hello, World!")

# 6. Example
with open("file.txt", "b") as file:
    file.write("Hello, World!")

# 7. Example
with open("file.txt", "t") as file:
    file.write("Hello, World!")
