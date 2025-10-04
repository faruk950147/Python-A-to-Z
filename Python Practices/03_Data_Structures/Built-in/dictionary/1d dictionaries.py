# ============================= 1. What is Dictionary =============================
# → Dictionary is a collection of key-value pairs
# → every key is unique
# → Dictionary is mutable (change possible)
# → Python 3.7+ is ordered
# → key is indexed
# → loop is iterable
# → reference type, dynamic type, hash table based

# ============================= 2. Basic Dictionary =============================
# Dictionary creation

# using {} 1d
dict1 = {"name": "John", "age": 30}

# using dict() constructor 1d
dict2 = dict(name="John", age=30)

# dictionary access (key based)
print(dict1["name"])  # John
print(dict2["age"])   # 30

# dictionary modify
dict1["age"] = 31
dict2["age"] = 31

# add new key-value
dict1["city"] = "New York"
dict2["city"] = "New York"

# ============================= 3. Dictionary Access Functions =============================
dict3 = {"name": "Alice", "age": 25, "city": "London"}
# show dictionary
print(dict3)

# direct access
print(dict3["name"])  

# get() → key not found, return None or default value
print(dict3.get("country"))        # None
print(dict3.get("country", "N/A")) # N/A

# keys(), values(), items()
print(dict3.keys())    # dict_keys(['name', 'age', 'city'])
print(dict3.values())  # dict_values(['Alice', 25, 'London'])
print(dict3.items())   # dict_items([('name', 'Alice'), ('age', 25), ('city', 'London')])

# ============================= 4. Dictionary Add Functions =============================
dict4 = {"a": 1, "b": 2}
dict4["a"] = 3
dict4.update({"c": 3, "d": 4})  # add new key or replace existing value
print(dict4)   # {'a': 3, 'b': 2, 'c': 3, 'd': 4}

# setdefault() → add new key if not exists, do nothing if exists
dict4.setdefault("e", 5)
print(dict4)   # {'a': 3, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# ============================= 5. Dictionary Modify Functions =============================
dict4["a"] = 3
dict4.update({"c": 3, "d": 4})  # add new key or replace existing value
print(dict4)   # {'a': 3, 'b': 2, 'c': 3, 'd': 4}

# setdefault() → add new key if not exists, do nothing if exists
dict4.setdefault("e", 5)
print(dict4)   # {'a': 3, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# ============================= 6. Dictionary Delete Functions =============================
dict7 = {"name": "John", "age": 30, "city": "New York"}

# delete specific key
del dict7["name"]

# pop() → delete specific key and return value
age_value = dict7.pop("age")
print("Popped age:", age_value)

# popitem() → delete last inserted key-value
last_item = dict7.popitem()
print("Last item:", last_item)

# clear() → remove all items
dict7.clear()
print(dict7)   # {}

# del → delete entire dictionary
del dict7

# ============================= 7. Looping Dictionary =============================
dict8 = {"x": 10, "y": 20, "z": 30}

# loop through keys
for k in dict8.keys():
    print("Key:", k)

# loop through values
for v in dict8.values():
    print("Value:", v)

# loop through key-value pairs
for k, v in dict8.items():
    print("Key:", k, "Value:", v)

# ============================= 8. Dictionary Comprehension =============================
# create a dictionary with squares
squares = {x: x*x for x in range(1, 6)}
print(squares)  # {1:1, 2:4, 3:9, 4:16, 5:25}

# filter only even numbers
evens = {x: x for x in range(10) if x % 2 == 0}
print(evens)   # {0:0, 2:2, 4:4, 6:6, 8:8}

# ============================= 9. Dictionary condition Functions =============================
dict1 = {"name": "John", "age": 31, "city": "New York"}

# Find keys with specific value
values = [25, 31]
result = {k: v for k, v in dict1.items() if v in values}
print(result)   # {'age': 31}

# Search key
key = "city"
if key in dict1:
    print(dict1[key])   # New York
else:
    print("Key not found")

