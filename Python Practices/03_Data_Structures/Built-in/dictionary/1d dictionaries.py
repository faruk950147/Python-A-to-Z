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

# copy()
dict4 = dict3.copy()

# clear()
dict3.clear()

# get()
dict3.get("name")

# items()
dict3.items()

# keys()
dict3.keys()

# values()
dict3.values()

# pop()
dict3.pop("name", None)

# popitem()
dict3.popitem()

# setdefault()
dict3.setdefault("name", "John")

# update()
dict3.update({"age": 31})

# fromkeys()
dict3.fromkeys(["name", "age"], "John")

# 4. ============================= dictionary operations ============================
# → Operations like len(), in/not in, merge (| operator), key check, etc.
dict4 = {"name": "John", "age": 30}

# len()
len(dict4)

# in/not in
"name" in dict4

# merge (| operator)
dict4 | dict3

# key check
"name" in dict4

# 5. ============================= dictionary iteration =============================
# → Iterating with for loops: keys, values, items
for key in dict4:
    print(key)

for value in dict4.values():
    print(value)

for key, value in dict4.items():
    print(key, value)

for item in dict4.keys():
    print(item)

for item in dict4.values():
    print(item)

for item in dict4.items():
    print(item)

# 6. ============================= dictionary deletion ==============================
# → del dict[key]  
# Related to pop(), popitem(), clear()
dict5 = {"name": "John", "age": 30}
del dict5["name"]
dict5.pop("age")
dict5.popitem()
dict5.clear()
del dict5

# 7. ============================= dictionary copy ==================================
# → dict.copy()
dict6 = {"name": "John", "age": 30}
dict7 = dict6.copy()

# 8. ============================= dictionary clear =================================
# → dict.clear()  
# Deletion family method (removes everything)
dict6.clear()

# 9. ============================= dictionary update ================================
# → dict.update({key: value})  
# Related to setdefault()
dict6.update({"name": "John", "age": 30})

# 10. ============================= dictionary fromkeys ==============================
# → dict.fromkeys([keys], default_value)
dict6.fromkeys(["name", "age"], "John")

# 11. ============================= dictionary get ==================================
# → dict.get(key, default_value)
dict6.get("name")

# 12. ============================= dictionary items ================================
# → dict.items()
dict6.items()

# 13. ============================= dictionary keys =================================
# → dict.keys()
dict6.keys()

# 14. ============================= dictionary values ===============================
# → dict.values()
dict6.values()

# 15. ============================= dictionary pop ==================================
# → dict.pop(key)  
# Deletion family method
dict6.pop("name")

# 16. ============================= dictionary popitem ==============================
# → dict.popitem() (removes the last inserted item)  
# Deletion family method
dict6.popitem()

# 17. ============================= dictionary setdefault ===========================
# → dict.setdefault(key, default_value)  
# Related to update()
dict6.setdefault("name", "John")

# ============================= practical use cases =========================
# - Data processing
dict8 = {"name": "John", "age": 30}
dict9 = {"name": "John", "age": 30}
dict8 == dict9
# - Business logic
dict8.get("name")
dict9.get("name")
dict8.get("name") == dict9.get("name")
# - Algorithm implementation

# ============================= dictionary merge =============================
dict10 = {"name": "John", "age": 30}
dict11 = {"name": "John", "age": 30}
dict10 | dict11
