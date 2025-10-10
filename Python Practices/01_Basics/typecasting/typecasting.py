"""
Typecasting in Python

Definition:
Typecasting (or type conversion) in Python means converting a value from one data type to another.

Python supports two types of typecasting:

1. Implicit Typecasting

Python automatically converts one data type to another without user intervention.

Happens mostly when performing operations between different types.
"""

# ======================= 1. directly possible =======================
# ======================== int ========================
# int → int	int(10)	10
# 1.example
print(int(10)) # 10

# 2.example
print(int("10")) # 10
# ======================== float ========================
# int → float	float(10)	10.0
# 1.example
print(float(10)) # 10.0

# 2.example
print(float("10")) # 10.0
# ======================== complex ========================
# int → complex	complex(10)	10+0j
# 1.example
print(complex(10)) # 10+0j

# 2.example
print(complex("10")) # 10+0j
# ======================== bool ========================
# int → bool	bool(10)	True
# 1.example
print(bool(10)) # True

# 2.example
print(bool("10")) # True
# ======================== str ========================
# int → str	str(10)	'10'
# 1.example
print(str(10)) # '10'

# 2.example
print(str("10")) # '10'



# ======================= 2. directly not possible =======================

# int → list	list(10) TypeError, int iterable is not possible because int is not iterable
# 1.example
print(list(10)) # TypeError

# 2.example
print(list("10")) # TypeError

# int → tuple	tuple(10)	 TypeError, int iterable is not possible because int is not iterable
# 1.example
print(tuple(10)) # TypeError

# 2.example
print(tuple("10")) # TypeError

# int → set	set(10)	 TypeError, int iterable is not possible because int is not iterable
# 1.example
print(set(10)) # TypeError

# 2.example
print(set("10")) # TypeError


# ======================= 3. multiple possible =======================

# int → list (digit-wise)	list(str(10)) ['1','0']
# 1.example
print(list(str(10))) # ['1','0']

# 2.example
print(list("10")) # ['1','0']

# int → tuple (digit-wise)	tuple(str(10)) ('1','0')
# 1.example
print(tuple(str(10))) # ('1','0')

# 2.example
print(tuple("10")) # ('1','0')

# int → set (digit-wise)	set(str(10)) {'0','1'}
# 1.example
print(set(str(10))) # {'0','1'}

# 2.example
print(set("10")) # {'0','1'}

# int → list (single element)	[10]	 [10]
# 1.example
print([10]) # [10]
# 2.example
print([10]) # [10]

# int → tuple (single element)	(10,)	 (10,)
# 1.example
print((10,)) # (10,)
# 2.example
print((10,)) # (10,)

# int → set (single element)	{10}	 {10}
# 1.example
print({10}) # {10}
# 2.example
print({10}) # {10}

