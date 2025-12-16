# swap two numbers without using a temporary variable
a = 10
b = 20
a, b  = b, a # a, b left hand side = b, a right hand side
print("a =", a)
print("b =", b)

# swap two numbers using a temporary variable
a = 10
b = 20
temp = a
a = b
b = temp
print("a =", a)
print("b =", b)
