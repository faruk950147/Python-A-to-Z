# 1. ============================= What is dictionary ================================
# → What is a dictionary in Python, how it works, key-value concept
# dictionary is a collection of key-value pairs where each key is unique
# dictionary is mutable
# dictionary is ordered (as of Python 3.7)
# dictionary is indexed
# dictionary is iterable
# dictionary is a reference type
# dictionary is a dynamic type
# dictionary is a mutable type
# dictionary is a collection type
# dictionary is a data structure
# dictionary is a container type
# dictionary is a hash table
# dictionary is a map
# dictionary is a dictionary

# 2. ============================= basic dictionary =============================
# Simple examples of dictionary
# → How to create a dictionary (using {}, dict() constructor)
# How to use dictionary
# → How to access dictionary values (using keys)
# → How to modify dictionary values (using keys)
# → How to add new key-value pairs
# → How to remove key-value pairs

# using {}
dict1 = {"name": "John", "age": 30}

# using dict() constructor
dict2 = dict(name="John", age=30)

# access dictionary values (using keys)
print(dict1["name"])
print(dict2["age"])

# modify dictionary values (using keys)
dict1["age"] = 31
dict2["age"] = 31

# add new key-value pairs
dict1["city"] = "New York"
dict2["city"] = "New York"

# remove key-value pairs
dict1.pop("age")
dict2.pop("age")

# 3. ============================= dictionary methods ===============================
# → List of all dictionary methods (copy(), clear(), get(), items(), etc.)
dict3 = {"name": "John", "age": 30}
dict4 = dict3.copy() # creates a new dictionary with the same key-value pairs


# 5. ============================= dictionary iteration =============================
# → Iterating with for loops: keys, values, items
for key in dict4:
    print(key) # returns the keys in the dictionary

for value in dict4.values():
    print(value) # returns the values in the dictionary

for key, value in dict4.items():
    print(key, value) # returns the key-value pairs in the dictionary

for item in dict4.keys():
    print(item) # returns the keys in the dictionary

for item in dict4.values():
    print(item) # returns the values in the dictionary

for item in dict4.items():
    print(item) # returns the key-value pairs in the dictionary

# 6. ============================= dictionary deletion ==============================
# → del dict[key]  
# Related to pop(), popitem(), clear()
dict5 = {"name": "John", "age": 30}
del dict5["name"] # removes the specified key
dict5.pop("age") # removes the specified key
dict5.popitem() # removes the last inserted item
dict5.clear() # removes all key-value pairs
del dict5 # removes the dictionary

# 7. ============================= dictionary copy ==================================
# → dict.copy()
dict6 = {"name": "John", "age": 30}
dict7 = dict6.copy() # creates a new dictionary with the same key-value pairs

# 8. ============================= dictionary clear =================================
# → dict.clear()  
# Deletion family method (removes everything)
dict6.clear() # removes all key-value pairs

# 9. ============================= dictionary update ================================
# → dict.update({key: value})  
# Related to setdefault()
dict6.update({"name": "John", "age": 30})

# 10. ============================= dictionary fromkeys ==============================
# → dict.fromkeys([keys], default_value)
dict6.fromkeys(["name", "age"], "John")

# 11. ============================= dictionary get ==================================
# → dict.get(key, default_value)
dict6.get("name") # returns the value for the specified key

# 12. ============================= dictionary items ================================
# → dict.items()
dict6.items() # returns a view object that displays a list of dictionary's (key, value) tuple pairs

# 13. ============================= dictionary keys =================================
# → dict.keys()
dict6.keys() # returns a view object that displays a list of all the keys in the dictionary

# 14. ============================= dictionary values ===============================
# → dict.values()
dict6.values() # returns a view object that displays a list of all the values in the dictionary

# 15. ============================= dictionary pop ==================================
# → dict.pop(key)  
# Deletion family method
dict6.pop("name")    # removes the specified key

# 16. ============================= dictionary popitem ==============================
# → dict.popitem() (removes the last inserted item)  
# Deletion family method
dict6.popitem() # removes the last inserted item

# 17. ============================= dictionary setdefault ===========================
# → dict.setdefault(key, default_value)  
# Related to update()
dict6.setdefault("name", "John") # returns the value for the specified key, if key is not found, insert the key with the specified value

# ============================= practical use cases =========================
# - Data processing
dict8 = {"name": "John", "age": 30}
dict9 = {"name": "John", "age": 30}
dict8 == dict9 # returns True if the dictionaries are equal
# - Business logic
dict8.get("name") # returns the value for the specified key
dict9.get("name") # returns the value for the specified key
dict8.get("name") == dict9.get("name") # returns True if the values are equal
# - Algorithm implementation

# ============================= dictionary merge =============================
dict10 = {"name": "John", "age": 30}
dict11 = {"name": "John", "age": 30}
dict10 | dict11 # merges two dictionaries
