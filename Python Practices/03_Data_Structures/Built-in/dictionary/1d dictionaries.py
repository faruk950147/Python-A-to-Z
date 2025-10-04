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
