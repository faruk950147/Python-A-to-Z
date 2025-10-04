# ============================= 1. What is Dictionary =============================
# → Dictionary is a collection of key-value pairs
# → every key is unique
# → Dictionary is mutable (change possible)
# → Python 3.7+ is ordered
# → key is indexed
# → loop is iterable
# → reference type, dynamic type, hash table based

# ============================= 2. Basic Dictionary =============================

# Dictionary of Dictionaries
dict1 = {
    "person1": {
        "name": "John",
        "age": 30,
        "city": "New York"
    },
    "person2": {
        "name": "Jane",
        "age": 25,
        "city": "Los Angeles"
    }
}

# List of Dictionaries
dict_list = [
    {
        "name": "John",
        "age": 30,
        "city": "New York"
    },
    {
        "name": "Jane",
        "age": 25,
        "city": "Los Angeles"
    }
]

# ============================= 3. Dictionary Access Functions =============================

# direct access
print(dict1["person1"]["name"])   # John
print(dict_list[1]["city"])       # Los Angeles

# get() → key not found, return None or default value
print(dict1.get("person3"))                  # None
print(dict1.get("person3", "Not Found"))     # Not Found

# keys(), values(), items()
print(dict1.keys())    
print(dict1.values())  
print(dict1.items())   

# ============================= 4. Dictionary Add Functions =============================
dict1["person1"]["age"] = 31   # modify
dict1.update({"person3": {"name": "Alice", "age": 28, "city": "Chicago"}})
dict1.setdefault("person4", {"name": "Bob", "age": 22, "city": "Miami"})
print(dict1)

# ============================= 5. Dictionary Modify Functions =============================
dict1["person1"]["age"] = 31   # modify
dict1.update({"person3": {"name": "Alice", "age": 28, "city": "Chicago"}})
dict1.setdefault("person4", {"name": "Bob", "age": 22, "city": "Miami"})
print(dict1)

# ============================= 5. Dictionary Delete Functions =============================
# delete specific key
del dict1["person2"]

# pop() → delete specific key and return value
removed = dict1.pop("person3")
print("Removed:", removed)

# popitem() → delete last inserted key-value
last_item = dict1.popitem()
print("Last item:", last_item)

# clear() → remove all items
dict1.clear()
print(dict1)

# ============================= 6. Looping Dictionary =============================
for key, value in dict_list[0].items():
    print(f"{key} → {value}")

# ============================= 7. Dictionary Comprehension =============================
# create a dictionary with squares
squares = {x: x*x for x in range(1, 6)}
print(squares)

# filter only even numbers
evens = {x: x for x in range(10) if x % 2 == 0}
print(evens)
