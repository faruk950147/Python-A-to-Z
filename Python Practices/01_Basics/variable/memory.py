a = [1, 2, 3]
print(id(a))        # this will show the memory address of a
print(hex(id(a)))   # this will show the memory address of a in hex
b = a
print(id(b))        # this will show the memory address of b
print(hex(id(b)))   # this will show the memory address of b in hex


x = [1, 2, 3]
y = x
z = [1, 2, 3]

print(id(x) == id(y))   # True, because x and y are the same object
print(id(x) == id(z))   # False, because z is a new object
