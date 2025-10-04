"""
# =================== Python Datatypes ===================
1. primitive datatypes
   - int      → 10, -5, 1000
   - float    → 3.14, -0.5
   - complex  → 2+3j
   - bool     → True, False
   - NoneType → None
   - bytes    → b"hello"
   - bytearray → bytearray([65, 66, 67])
   - memoryview→ memoryview(b"hello")  
2. non-primitive datatypes
   - str      → "Hello", 'Python'
   - list     → [1, 2, 3]
   - tuple    → (1, 2, 3)
   - set      → {1, 2, 3}
   - dict     → {"name": "Faruk", "age": 20}
Python Datatypes (Quick Notes)
==============================

1. Numbers
   - int      → 10, -5, 1000
   - float    → 3.14, -0.5
   - complex  → 2+3j

2. Text
   - str      → "Hello", 'Python'

3. Boolean
   - bool     → True, False

4. Sequence Types
   - list     → [1, 2, 3]
   - tuple    → (1, 2, 3)
   - range    → range(5) → 0 to 4

5. Set Types
   - set      → {1, 2, 3}
   - frozenset→ frozenset({1, 2, 3})

6. Mapping
   - dict     → {"name": "Faruk", "age": 20}

7. Binary Types
   - bytes     → b"hello"
   - bytearray → bytearray([65, 66, 67])
   - memoryview→ memoryview(b"hello")
"""
# Example:

a = 10
b = 3.14
c = "Python"
d = True
e = [1, 2, 3]
f = (1, 2, 3)
g = {"x", "y"}
h = {"name": "Faruk", "age": 20}

print(type(a))  # <class 'int'>
print(type(b))  # <class 'float'>
print(type(c))  # <class 'str'>
print(type(d))  # <class 'bool'>
print(type(e))  # <class 'list'>
print(type(f))  # <class 'tuple'>
print(type(g))  # <class 'set'>
print(type(h))  # <class 'dict'>

 # Type Conversion

x = 10
y = 3.14
z = "10"

print(int(x))  # 10
print(float(y))  # 3.14
print(int(z))  # 10
print(str(z))  # "10"
