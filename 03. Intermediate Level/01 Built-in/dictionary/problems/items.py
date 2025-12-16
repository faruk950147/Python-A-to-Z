# items() returns a view object that displays a list of dictionary's 
# (key, value) tuple pairs

dict1 = {'name': 'Faruk', 'age': 21, 'gender': 'Male'}
print(dict1.items())
for key, value in dict1.items():
    print(f"Keys {key} ======> Values {value}")