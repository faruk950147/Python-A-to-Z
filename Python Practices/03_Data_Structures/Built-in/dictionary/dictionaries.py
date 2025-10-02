# 1. ============================= What is dictionary ================================
# → What is a dictionary in Python, how it works, key-value concept

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
print(dict2["name"])

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

# 4. ============================= dictionary operations ============================
# → Operations like len(), in/not in, merge (| operator), key check, etc.

# 5. ============================= dictionary iteration =============================
# → Iterating with for loops: keys, values, items

# 6. ============================= dictionary deletion ==============================
# → del dict[key]  
# Related to pop(), popitem(), clear()

# 7. ============================= dictionary copy ==================================
# → dict.copy()

# 8. ============================= dictionary clear =================================
# → dict.clear()  
# Deletion family method (removes everything)

# 9. ============================= dictionary update ================================
# → dict.update({key: value})  
# Related to setdefault()

# 10. ============================= dictionary fromkeys ==============================
# → dict.fromkeys([keys], default_value)

# 11. ============================= dictionary get ==================================
# → dict.get(key, default_value)

# 12. ============================= dictionary items ================================
# → dict.items()

# 13. ============================= dictionary keys =================================
# → dict.keys()

# 14. ============================= dictionary values ===============================
# → dict.values()

# 15. ============================= dictionary pop ==================================
# → dict.pop(key)  
# Deletion family method

# 16. ============================= dictionary popitem ==============================
# → dict.popitem() (removes the last inserted item)  
# Deletion family method

# 17. ============================= dictionary setdefault ===========================
# → dict.setdefault(key, default_value)  
# Related to update()

# ============================= practical use cases =========================
# - Data processing
# - Business logic
# - Algorithm implementation
