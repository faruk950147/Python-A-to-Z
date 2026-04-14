# =================== memory address deference ===================
# always create new object and assign to a
a = 10
print('Value of a first line:', a)
print('ID of a first line:', id(a))

# create new object and assign to a
a = a + 20  
print('Value of a second line:', a)
print('ID of a second line:', id(a))

# create new object and assign to b
# immutable object
b = 10  
print('Value of b third line:', b)
print('ID of b third line:', id(b))

# create new object and assign to b
# immutable object
b += 20  
print('Value of b fourth line:', b)
print('ID of b fourth line:', id(b))

# =================== list (mutable vs immutable behavior) ===================
a = [1, 2, 3]
print('Value of a list:', a)
print('ID of a list:', id(a))

# always create new object and assign to a
a = a + [4, 5, 6]  
print('Value of a list:', a)
print('ID of a list:', id(a))

# modify same object (mutable behavior)
a += [4, 5, 6]
print('Value of a list:', a)
print('ID of a list:', id(a))