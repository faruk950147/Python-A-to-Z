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
string1 = "Hello World"

print(f"Slice string1 [1:3]: {string1[1:3]}")   
# "el" → starts from index 1 ("e"), stops before index 3 ("l"), step = 1

print(f"Slice string1 [:3]: {string1[:3]}")     
# "Hel" → start is missing, so defaults to 0, stops before index 3, step = 1

print(f"Slice string1 [0:]: {string1[0:]}")     
# "Hello World" → starts from index 0, end is missing so goes till the end

print(f"Slice string1 [:]: {string1[:]}")       
# "Hello World" → start is missing (0), end is missing (till the end), so the whole string

print(f"Slice string1 [::]: {string1[::]}")     
# "Hello World" → same as [:], because step is missing so default step = 1

print(f"Slice string1 [::2]: {string1[::2]}")   
# "HloWrd" → start = 0, end = till the end, step = 2 (takes every 2nd character)

print(f"Slice string1 [::3]: {string1[::3]}")   
# "HlWl" → start = 0, end = till the end, step = 3 (takes every 3rd character)

# =============================== Negative Indexing ===============================
print("\n============================ Negative Indexing =============================")
print(f"Slice string1 [-1]: {string1[-1]}")   
# "!" → starts from the end, stops before index 0, step = 1

print(f"Slice string1 [-2:]: {string1[-2:]}")   
# "d" → starts from the end, stops before index 0, step = 1

print(f"Slice string1 [:-2]: {string1[:-2]}")   
# "Hello Wor" → starts from index 0, stops before index -2, step = 1


print(f"Slice string1 [-2:-1]: {string1[-2:-1]}")   
# "d" → starts from the end, stops before index 0, step = 1

print(f"Slice string1 [-2:-3]: {string1[-2:-3]}")   
# "d" → starts from the end, stops before index 0, step = 1

# Reverse String
print("\n============================ String Reverse =============================")
print(f"Slice string1 [::-1]: {string1[::-1]}")   
# "dlroW olleH" → start = 0, end = till the end, step = -1 (takes every character in reverse)

print(f"Slice string1 [::-2]: {string1[::-2]}")   
# "dlroW olleH" → start = 0, end = till the end, step = -2 (takes every 2nd character in reverse)

print(f"Slice string1 [::-3]: {string1[::-3]}")   
# "dlroW olleH" → start = 0, end = till the end, step = -3 (takes every 3rd character in reverse)

print(f"Slice string1 [::-4]: {string1[::-4]}")   
# "dlroW olleH" → start = 0, end = till the end, step = -4 (takes every 4th character in reverse)



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
for i in range(len(string1)):
    print(string1[i], end=" ")  # every character is printed separately
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
