# ============================= 1. What is String =============================
# → String is a sequence of characters in a specific order
# → Characters can repeat (not unique)
# → String is immutable (cannot be changed directly)
# → Always ordered (index based)
# → Iterable (can use loop)
# → Reference type, dynamic type
# → Stored in contiguous memory (not hash table)

# ============================= 2. Basic String =============================
print("\n============================ String Creation =============================")
string1 = "Hello, World!" # double quotes
string2 = 'Hello, World!' # single quotes
string3 = """Hello, World!""" # triple quotes
print("string1 (created):", string1)
print("string2 (created):", string2)
print("string3 (created):", string3)

# ============================= 3. String Access Functions =============================
print("\n============================ String Access Functions =============================")
print("string1 (accessed):", string1)

# String Slicing
print("\n============================ String Slicing =============================")
print(f"Slice string1 [1:3]: {string1[1:3]}")           # el
print(f"Reverse using slicing: {string1[::-1]}")       # !dlroW olleH
print(f"First 3 elements: {string1[:3]}")              # Hel
print(f"Last 2 elements: {string1[-2:]}")              # d!
print(f"From index 3 to end: {string1[3:]}")           # lo, World!
print(f"Alternate elements: {string1[::2]}")           # Hlo ol!
print(f"Reverse alternate elements: {string1[::-2]}")  # !drWolH
print(f"Alternate elements from index 1: {string1[1::2]}")  # el,Wrd
print(f"Alternate elements from index -2: {string1[-2::-2]}") # dW,le
print(f"Alternate elements from index -1: {string1[-1::-2]}") # !o lH

# ============================= 4. String Add Functions =============================
print("\n============================ String Add Functions =============================")
string2 = "Python"
print("Concatenation:", string1 + " " + string2)  # Hello, World! Python

# ============================= 5. String Modify Functions =============================
print("\n============================ String Modify Functions =============================")
print("Replace 'World' with 'Python':", string1.replace("World", "Python"))
print("Uppercase:", string1.upper())
print("Lowercase:", string1.lower())
print("Title Case:", string1.title())

# ============================= 6. String Delete Functions =============================
print("\n============================ String Delete Functions =============================")
# Direct delete string immutable
# but replace using new string string immutable
print("Remove 'World':", string1.replace("World", ""))  # "Hello, !"

# ============================= 7. Looping String =============================
print("\n============================ Looping String =============================")
for char in string1:
    print(char, end=" ")  # every character is printed separately

# ============================= 8. String Comprehension =============================
print("\n\n============================ String Comprehension =============================")
comp_list = [ch for ch in string1]
print("Comprehension result:", comp_list)

# ============================= 9. String Condition Functions =============================
print("\n============================ String Condition Functions =============================")
string2 = "Hello, World!"
print("Equal check:", string1 if string1 == string2 else "Not Equal")
print("Starts with 'Hello'? ->", string1.startswith("Hello"))
print("Ends with 'World!'? ->", string1.endswith("World!"))
print("Is alphabetic? ->", string1.isalpha())   # False (because of space)
print("Is digit? ->", string1.isdigit())       # False
print("Contains 'Hello'? ->", "Hello" in string1)
