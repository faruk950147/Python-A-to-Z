# ============================= Format Operator Functions =============================
string3 = "Hello World"
print("My string is: %s" % string3)

num = 10
print("My number is: %d" % num)
num2 = 10.5
print("My number is: %f" % num2)
bin_num = 0b1010
print("My binary number is: %d" % bin_num)
# f-string (Python 3.6+)
print(f"Row string: {string3}")

# format() simple placeholder
print("Row string: {str_var}".format(str_var="Hello World"))


