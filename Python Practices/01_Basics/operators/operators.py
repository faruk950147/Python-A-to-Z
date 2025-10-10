# operator and operand
# operator = + # operator is an operator 
# operand = 10 # operand is a value

# operator precedence and associativity
# operator precedence is the order in which operators are evaluated
# associativity is the order in which operators are evaluated


# 1. ======================= Arithmetic operators =======================
# Arithmetic operators is a symbol that is used to perform arithmetic operations.

# + addition
# - subtraction
# * multiplication
# / division // floor division
# % modulo
# ** exponentiation
# ~ absolute value

# 1. example
a = 10
b = 20
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)
print(-a)


# 2. ======================= Assignment operators =======================
# Assignment operators is a symbol that is used to assign a value to a variable.

# = assignment
# += addition assignment
# -= subtraction assignment
# *= multiplication assignment
# /= division assignment
# %= modulo assignment
# **= exponentiation assignment

# 2. example
x = 10
x += 20
print(x)


# 3. ======================= Comparison operators =======================
# Comparison operators is a symbol that is used to compare two values.

# == equal to
# != not equal to
# > greater than
# < less than
# >= greater than or equal to
# <= less than or equal to

# 3. example
a = 10
b = 20
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)


# 4. ======================= Logical operators =======================
# Logical operators is a symbol that is used to perform logical operations.

# and logical and
# or logical or
# not logical not

# 4. example
a = 10
b = 20
print(a and b)
print(a or b)
print(not a)


# 5. ======================= Bitwise operators =======================
# Bitwise operators is a symbol that is used to perform bitwise operations.

# & bitwise AND
# | bitwise OR
# ^ bitwise XOR
# ~ bitwise NOT
# << left shift
# >> right shift

# 5. example
a = 10
b = 20
print(a & b)
print(a | b)
print(a ^ b)
print(~a)
print(a << b)
print(a >> b)


# 6. ======================= Membership operators =======================
# Membership operators is a symbol that is used to perform membership operations.

# in membership
# not in membership

# 6. example
a = [10, 20, 30]
print(10 in a)
print(10 not in a)


# 7. ======================= Identity operators =======================
# Identity operators is a symbol that is used to perform identity operations.

# is identity
# is not identity

# 7. example
a = 10
b = 20
print(a is b)
print(a is not b)


# 8. ======================= walrus operator =======================
# Walrus operator is a symbol that is used to assign a value to a variable.

# := walrus operator

# 8. example
if (i := 10) > 10:
    print(i)
else:
    print(i)
while (i := 10) > 10:
    print(i)

# 9. ======================= Ternary operators =======================
# Ternary operators is a symbol that is used to perform ternary operations.

# condition_if_true if condition else condition_if_false

# 9. example
a = 10
b = 20
print(a if a > b else b)


# 10. ======================= Other operators =======================
# Other operators is a symbol that is used to perform other operations.

# yield yield
# lambda lambda
# @ operator

# 10. example
print((lambda x, y: x + y)(10, 20))
print((lambda x, y: x + y)(10, 20))
print((lambda x, y: x + y)(10, 20))

