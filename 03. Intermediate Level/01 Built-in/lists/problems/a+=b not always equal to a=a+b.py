# =================== memory address deference ===================
# always create new object and assign to a
a = 10
print('Value of a first line:', a)
print('ID of a first line:', id(a))
a = a + 20 # create new object and assign to a
print('Value of a second line:', a)
print('ID of a second line:', id(a))

b = 10 # immutable object
print('Value of b third line:', b)
print('ID of b third line:', id(b))
b += 20 # create new object and assign to a
print('Value of b fourth line:', b)
print('ID of b fourth line:', id(b))

# =================== memory address deference ===================
# always create new object and assign to a
a = [1, 2, 3]
print('Value of a list:', a)
print('ID of a list:', id(a))

# always create new object and assign to a
a = a + [4, 5, 6]
print('Value of a list:', a)
print('ID of a list:', id(a))

# always create new object and assign to a
a += [4, 5, 6] # append to the same object
print('Value of a list:', a)
print('ID of a list:', id(a))
