# copy()
dict4 = dict3.copy() # creates a new dictionary with the same key-value pairs

# clear()
dict3.clear() # removes all key-value pairs

# get()
dict3.get("name") # returns the value for the specified key

# items()
dict3.items() # returns a view object that displays a list of dictionary's (key, value) tuple pairs

# keys()
dict3.keys() # returns a view object that displays a list of all the keys in the dictionary

# values()
dict3.values() # returns a view object that displays a list of all the values in the dictionary

# pop()
dict3.pop("name", None) # removes the specified key and returns the value

# popitem()
dict3.popitem() # if value available removes the last inserted item else returns error

# setdefault()
dict3.setdefault("name", "John") # returns the value for the specified key, if key is not found, insert the key with the specified value

# update()
dict3.update({"age": 31}) # updates the dictionary with the specified key-value pairs

# fromkeys()
dict3.fromkeys(["name", "age"], "John") # returns a new dictionary with the specified keys and values

# 4. ============================= dictionary operations ============================
# → Operations like len(), in/not in, merge (| operator), key check, etc.
dict4 = {"name": "John", "age": 30}

# len()
len(dict4) # returns the number of key-value pairs in the dictionary

# in/not in
"name" in dict4 # returns True if the specified key is in the dictionary

# merge (| operator)
dict4 | dict3 # merges two dictionaries

# key check
"name" in dict4 # returns True if the specified key is in the dictionary