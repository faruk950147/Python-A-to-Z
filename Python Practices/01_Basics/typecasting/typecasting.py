"""
Typecasting in Python

Definition:
Typecasting (or type conversion) in Python means converting a value from one data type to another.

Python supports two types of typecasting:

1. Implicit Typecasting

Python automatically converts one data type to another without user intervention.

Happens mostly when performing operations between different types.
"""

# Example:

a = 5        # int
b = 2.5      # float

c = a + b    # 'a' is converted to float automatically
print(c)     # Output: 7.5
print(type(c))  # Output: <class 'float'>

"""
2. Explicit Typecasting

You manually convert a value from one type to another using built-in functions.

Common Functions:

int() → convert to integer

float() → convert to float

str() → convert to string

bool() → convert to boolean

list(), tuple(), set() → convert to list, tuple, set
"""

# Example:
# Implicit Typecasting
a = 5        # int
b = 2.5      # float
c = a + b    # int automatically converted to float
print(c, type(c))  # 7.5 <class 'float'>

# Explicit Typecasting (string to other types)
x = "10"
y = int(x)       # string → int
z = float(x)     # string → float
b_val = bool(x)  # string → bool
lst = list(x)    # string → list of characters
tpl = tuple(x)   # string → tuple of characters
st = set(x)      # string → set of characters (unique)

print(y, type(y))  # 10 <class 'int'>
print(z, type(z))  # 10.0 <class 'float'>
print(b_val, type(b_val))  # True <class 'bool'>
print(lst, type(lst))  # ['1','0'] <class 'list'>
print(tpl, type(tpl))  # ('1','0') <class 'tuple'>
print(st, type(st))  # {'0','1'} <class 'set'>

# Explicit Typecasting (int to other types)
num = 10
num_str = str(num)       # int → string
num_float = float(num)   # int → float
num_bool = bool(num)     # int → bool
num_list = [num]         # int → list (wrap manually)
num_tuple = (num,)       # int → tuple (wrap manually)
num_set = {num}          # int → set (wrap manually)

print(num_str, type(num_str))   # '10' <class 'str'>
print(num_float, type(num_float)) # 10.0 <class 'float'>
print(num_bool, type(num_bool))   # True <class 'bool'>
print(num_list, type(num_list))   # [10] <class 'list'>
print(num_tuple, type(num_tuple)) # (10,) <class 'tuple'>
print(num_set, type(num_set))     # {10} <class 'set'>

# Complex number
p = 3j
print(p, type(p))  # 3j <class 'complex'>



# impossible to convert
# int to list
# int to tuple

# a = 10
# b = list(a)
# # print(b, type(b))  # ['1', '0'] <class 'list'>

# c = tuple(a)
# print(c, type(c))  # ('1', '0') <class 'tuple'>

# d = set(a)
# print(d, type(d))  # {'1', '0'} <class 'set'>


