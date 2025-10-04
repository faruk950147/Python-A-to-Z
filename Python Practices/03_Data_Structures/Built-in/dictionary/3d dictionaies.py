# ============================= 1. What is Dictionary =============================
# → Dictionary is a collection of key-value pairs
# → every key is unique
# → Dictionary is mutable (change possible)
# → Python 3.7+ is ordered
# → key is indexed
# → loop is iterable
# → reference type, dynamic type, hash table based

# ============================= 2. Basic Dictionary =============================

# Dictionary of Dictionaries (3D)
dict1 = {
    "dept1": {
        "person1": {"name": "John", "age": 31, "city": "New York"},
        "person2": {"name": "Jane", "age": 25, "city": "Los Angeles"}
    },
    "dept2": {
        "person3": {"name": "Alice", "age": 28, "city": "London"},
        "person4": {"name": "Bob", "age": 35, "city": "Paris"}
    }
}

# List of Dictionaries (3D)
list1 = [
    {
        "dept1": {
            "person1": {"name": "John", "age": 31, "city": "New York"},
            "person2": {"name": "Jane", "age": 25, "city": "Los Angeles"}
        },
        "dept2": {
            "person3": {"name": "Alice", "age": 28, "city": "London"},
            "person4": {"name": "Bob", "age": 35, "city": "Paris"}
        }
    }
]

# ============================= 3. Dictionary Access Functions =============================

print(dict1["dept1"]["person1"]["name"])  # John
print(dict1["dept1"]["person2"]["age"])   # 25

print(list1[0]["dept1"]["person1"]["name"])  # John
print(list1[0]["dept1"]["person2"]["age"])   # 25

# ============================= 4. Dictionary Add Functions =============================
dict1["dept1"]["person3"] = {"name": "Alice", "age": 28, "city": "London"}
dict1["dept2"]["person4"] = {"name": "Bob", "age": 35, "city": "Paris"}

list1[0]["dept1"]["person3"] = {"name": "Alice", "age": 28, "city": "London"}
list1[0]["dept2"]["person4"] = {"name": "Bob", "age": 35, "city": "Paris"}

print(dict1)
print(list1)

# ============================= 5. Dictionary Modify Functions =============================
dict1["dept1"]["person1"]["age"] = 32
dict1["dept2"]["person4"]["age"] = 36   

list1[0]["dept1"]["person1"]["age"] = 32
list1[0]["dept2"]["person4"]["age"] = 36

print(dict1)
print(list1)

# ============================= 6. Dictionary Delete Functions =============================
dict1["dept1"].pop("person3")   # Delete specific key
dict1.pop("dept2")              # Delete entire department

list1[0]["dept1"].pop("person3")
list1[0].pop("dept2")

print(dict1)
print(list1)

# ============================= 7. Looping Dictionary =============================
for key, value in dict1.items():
    print(f"Department: {key}")
    for inner_key, inner_value in value.items():
        print(f"  Person: {inner_key}")
        for inner_inner_key, inner_inner_value in inner_value.items():
            print(f"    {inner_inner_key} → {inner_inner_value}")

for dic in list1:
    for key, value in dic.items():
        print(f"Department: {key}")
        for inner_key, inner_value in value.items():
            print(f"  Person: {inner_key}")
            for inner_inner_key, inner_inner_value in inner_value.items():
                print(f"    {inner_inner_key} → {inner_inner_value}")

# ============================= 8. Dictionary Comprehension =============================
squares = {x: x**2 for x in range(1, 6)}
print(squares)  

even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(even_squares)

# ============================= 9. Dictionary Condition Functions =============================
dictA = {"a": 1, "b": 2, "c": 3}
dictB = {"a": 1, "b": 2, "c": 3}
dictC = {"a": 1, "b": 5, "d": 9}

print(dictA == dictB)   # True
print(dictA == dictC)   # False

print("a" in dictA)     # True
print("z" in dictA)     # False

print(2 in dictA.values())   # True
print(9 in dictA.values())   # False

print(dictA.keys() & dictC.keys())   # {'a'}
print(dictA.keys() - dictC.keys())   # {'b', 'c'}

print(dictA.items() & dictC.items()) # {('a', 1)}
