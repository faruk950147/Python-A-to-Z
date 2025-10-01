"""
Typecasting in Python

Definition:
Typecasting (or type conversion) in Python means converting a value from one data type to another.

Python supports two types of typecasting:

1. Implicit Typecasting

Python automatically converts one data type to another without user intervention.

Happens mostly when performing operations between different types.
"""

# ======================= 1. possible =======================

# int → list (digit-wise)	list(str(10)) ['1','0']
# int → tuple (digit-wise)	tuple(str(10)) ('1','0')
# int → set (digit-wise)	set(str(10)) {'0','1'}
# int → list (single element)	[10]	 [10]
# int → tuple (single element)	(10,)	 (10,)
# int → set (single element)	{10}	 {10}

# ======================= 2. directly not possible =======================

# int → list	list(10)	❌ TypeError, int iterable is not possible because int is not iterable
# 1.example
print(list(10))

# 2.example
print(list("10"))

# int → tuple	tuple(10)	❌ TypeError, int iterable is not possible because int is not iterable
# 1.example
print(tuple(10))

# 2.example
print(tuple("10"))

# int → set	set(10)	❌ TypeError, int iterable is not possible because int is not iterable
# 1.example
print(set(10))

# 2.example
print(set("10"))

