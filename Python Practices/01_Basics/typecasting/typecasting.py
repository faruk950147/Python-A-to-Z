"""
Typecasting in Python
Definition:
Typecasting (or type conversion) in Python means converting a value from one data type to another.
Python supports two types of typecasting:
1. Implicit Typecasting
Python automatically converts one data type to another without user intervention.
Happens mostly when performing operations between different types.
            Example:
            a = 10
            b = 20.0
            print(a + b) # 30.0
            print(a + b + 30) # 60.0
            
2. Explicit Typecasting
Python converts the data type of an object to a required data type explicitly by the user.
user intervention is required.
            Example:
            x = "100"       # string
            y = int(x)      # string to int
            z = float(x)    # string to float

            print(x, type(x))  # Output: 100 <class 'str'>
            print(y, type(y))  # Output: 100 <class 'int'>
            print(z, type(z))  # Output: 100.0 <class 'float'>
            # float to int
            a = int(10.9)
            print(a)  # Output: 10

            # int to string
            b = str(50)
            print(b + " is a number")  # Output: 50 is a number

            # list to set
            c = [1, 2, 3, 3]
            print(set(c))  # Output: {1, 2, 3}


          
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

