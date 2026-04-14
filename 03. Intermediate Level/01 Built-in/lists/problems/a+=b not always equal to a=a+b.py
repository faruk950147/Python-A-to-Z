'''
1. Integer (Immutable behavior)
a = 10
a = a + 20
A new value is created each time
The original value is not modified
So the memory address (id) changes

2. Another Integer example
b = 10
b += 20
A new object is created again
The variable b now points to a new memory location
So the id changes

3. List (Mutable behavior)
a = [1, 2, 3]
Case 1:
a = a + [4, 5, 6]
A new list is created
The old list is not modified
So id changes

Case 2:
a += [4, 5, 6]
The existing list is modified in-place
No new object is created
So id stays the same

One-line summary:

This is a Python practice code that shows when a new object is created vs when the same object is modified in memory.

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

'''
# always create new object and assign to a
a = 10
print('Value of a first line:', a)
print('ID of a first line:', id(a))

# create new object and assign to a
a = a + 20  
print('Value of a second line:', a)
print('ID of a second line:', id(a))


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