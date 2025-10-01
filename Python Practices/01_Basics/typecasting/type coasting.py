# ===============================
# Python Typecasting Examples
# ===============================

print("===== Original Values =====")
a_int = 10
b_float = 3.14
c_str = "123"
d_bool = True
print("Integer:", a_int)
print("Float:", b_float)
print("String:", c_str)
print("Boolean:", d_bool)

# ===============================
# 1️⃣ Integer Conversions
# ===============================
print("\n===== Integer Conversions =====")
print("int -> float:", float(a_int))           # 10.0
print("int -> str:", str(a_int))               # '10'
print("int -> bool:", bool(a_int))             # True

# Iterable conversions
print("int -> list (digit-wise):", list(str(a_int)))   # ['1','0']
print("int -> tuple (digit-wise):", tuple(str(a_int))) # ('1','0')
print("int -> set (digit-wise):", set(str(a_int)))     # {'0','1'}

# Single element container
print("[a_int]:", [a_int])     # [10]
print("(a_int,):", (a_int,))   # (10,)
print("{a_int}:", {a_int})     # {10}

# ===============================
# 2️⃣ Float Conversions
# ===============================
print("\n===== Float Conversions =====")
print("float -> int:", int(b_float))       # 3
print("float -> str:", str(b_float))       # '3.14'
print("float -> bool:", bool(b_float))     # True

# Float -> iterable (digit-wise) using str
print("float -> list (digit-wise):", list(str(b_float)))   # ['3', '.', '1', '4']
print("float -> tuple (digit-wise):", tuple(str(b_float))) # ('3', '.', '1', '4')
print("float -> set (digit-wise):", set(str(b_float)))     # {'.','3','1','4'}

# Single element container
print("[b_float]:", [b_float])
print("(b_float,):", (b_float,))
print("{b_float}:", {b_float})

# ===============================
# 3️⃣ String Conversions
# ===============================
print("\n===== String Conversions =====")
str_num = "456"
str_alpha = "hello"

print("str_num -> int:", int(str_num))      # 456
print("str_num -> float:", float(str_num))  # 456.0
print("str_num -> bool:", bool(str_num))    # True

print("str_alpha -> bool:", bool(str_alpha)) # True

# String to iterable
print("str_alpha -> list:", list(str_alpha))   # ['h','e','l','l','o']
print("str_alpha -> tuple:", tuple(str_alpha)) # ('h','e','l','l','o')
print("str_alpha -> set:", set(str_alpha))     # {'e','h','o','l'}

# ===============================
# 4️⃣ Boolean Conversions
# ===============================
print("\n===== Boolean Conversions =====")
print("bool True -> int:", int(d_bool))       # 1
print("bool True -> float:", float(d_bool))   # 1.0
print("bool True -> str:", str(d_bool))       # 'True'
print("bool True -> list:", [d_bool])         # [True]
print("bool False -> bool:", bool(0))         # False

# ===============================
# 5️⃣ Container Conversions
# ===============================
print("\n===== Container Conversions =====")
lst = [1,2,3]
tpl = (4,5,6)
st = {7,8,9}

print("list -> tuple:", tuple(lst))   # (1,2,3)
print("list -> set:", set(lst))       # {1,2,3}

print("tuple -> list:", list(tpl))    # [4,5,6]
print("tuple -> set:", set(tpl))      # {4,5,6}

print("set -> list:", list(st))       # [7,8,9]
print("set -> tuple:", tuple(st))     # (7,8,9)


# ===============================
# 6️⃣ Other Conversions
# ===============================
print("\n===== Other Conversions =====")
print("int -> complex:", complex(a_int)) # 10+0j
print("float -> complex:", complex(b_float)) # 3.14+0j
print("str -> complex:", complex(c_str)) # ValueError, str is not a number
print("bool -> complex:", complex(d_bool)) # 1+0j


# Numeric conversions (int ↔ float, int/float ↔ bool, int/float ↔ str)

# String conversions (str ↔ int/float/bool, str → iterable)

# Boolean conversions (bool ↔ int/float/str, bool → container)

# Container conversions (list, tuple, set ↔ list, tuple, set)