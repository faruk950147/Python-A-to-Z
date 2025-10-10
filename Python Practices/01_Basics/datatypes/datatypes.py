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
# =================== primitive datatypes ===================
int = 10 # int      → 10, -5, 1000
float = 3.14 # float    → 3.14, -0.5
bool = True # bool     → True, False
complex = 2+3j # complex  → 2+3j
NoneType = None # NoneType → None
bytes = b"hello" # bytes    → b"hello"
bytearray = bytearray([65, 66, 67]) # bytearray → bytearray([65, 66, 67])
memoryview = memoryview(b"hello")  # memoryview→ memoryview(b"hello")

print(type(int))  # <class 'int'>
print(type(float))  # <class 'float'>
print(type(bool))  # <class 'bool'>
print(type(complex))  # <class 'complex'>
print(type(NoneType))  # <class 'NoneType'>
print(type(bytes))  # <class 'bytes'>
print(type(bytearray))  # <class 'bytearray'>
print(type(memoryview))  # <class 'memoryview'>



# =================== non-primitive datatypes ===================
# string
str = "Python" # str      → "Hello", 'Python'
# list
lst = [1, 2, 3] # list     → [1, 2, 3]
# tuple
tpl = (1, 2, 3) # tuple    → (1, 2, 3)
# set
st = {"x", "y"} # set      → {1, 2, 3}
# dictionary
dct = {"name": "Faruk", "age": 20} # dict     → {"name": "Faruk", "age": 20}

print(type(str))  # <class 'str'>
print(type(lst))  # <class 'list'>
print(type(tpl))  # <class 'tuple'>
print(type(st))  # <class 'set'>
print(type(dct))  # <class 'dict'>

