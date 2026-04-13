dict1 = {"name": "Faruk", "age": 22, "city": "Dhaka"}

# dict2 = dict(name="John", age=30, city="Dhaka")

# dict3 = dict([("name", "John"), ("age", 30), ("city", "Dhaka")])

# Accrss
# print(dict1)
# print(dict1["name"])

# modify
# dict1["name"]="Omar Faruk"
# print(dict1["name"])

# add
# dict1["Country"]="Bangladesh"
# print(dict1)

# print(dict1.get("country", "N/A"))
# print(dict1.keys())
# print(dict1.items())
# print(dict1.values())

# dict1.update({"Country": "Asia"})
# print(dict1)

# del dict1["name"]
# print(dict1)

# print(dict1.pop("name"))
# print(dict1)

# print(dict1.popitem())
# print(dict1)

# print(dict1.clear())
# print(dict1)

# for k in dict1.keys():
#     print("Key:", k)

# for v in dict1.values():
#     print("Value:", v)

# for k, v in dict1.items():
#     print("Key:", k, "Value:", v)
    
for index, key in enumerate(dict1, start=0):
    print("Index:", index, "Key:", key)
    
    
if "name" in dict1:
    print("Yes, 'name' is one of the keys in the dict1 dictionary")
else:
    print("No, 'name' is not one of the keys in the dict1 dictionary")


