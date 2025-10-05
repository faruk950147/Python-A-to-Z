# ============================= String Format Functions =============================

string3 = "Hello World"

# f-string (Python 3.6+)
print(f"Row string: {string3}")

# format() simple placeholder
print("Row string: {}".format(string3))

# format() keyword placeholder
print("Row string: {str_var}".format(str_var=string3))

# format() multiple placeholders
print("Row string: {str_var1} {str_var2}".format(str_var1=string3, str_var2="Python"))

# format() index placeholders
print("Row string: {0} {1}".format(string3, "Python"))

# format() named index placeholders
print("Row string: {str_var1} {str_var2}".format(str_var1=string3, str_var2="Python"))

# f-string with expression
str1 = "Python"
print(f"Row string: {string3 + ' ' + str1}")


# ============================= Numeric Format Functions =============================

# format() binary
print("Binary: {0:b}".format(10))     # 1010

# format() octal
print("Octal: {0:o}".format(10))      # 12

# format() hexadecimal
print("Hexadecimal: {0:x}".format(10))  # a

# format() integer (decimal)
print("Integer: {0:d}".format(10))    # 10

# format() float
print("Float: {0:f}".format(10.123456789))  # 10.123457 (default 6 decimal)

# Old style formatting (% operator)
a = 10
print("Integer: %d" % a)             # Integer: 10
print("Float: %f" % 10.123456789)    # Float: 10.123457
print("Float: %e" % 10.123456789)    # Float: 1.012346e+01
print("Float: %g" % 10.123456789)    # Float: 10.1235
print("Float: %G" % 10.123456789)    # Float: 10.1235
print("Hexadecimal: %x" % 10)        # Hexadecimal: a
print("Hexadecimal: %X" % 10)        # Hexadecimal: A


