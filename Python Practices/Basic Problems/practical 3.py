def even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(even_odd(10))

# swap two numbers
x = 10 # first number
y = 20 # second number
x, y = y, x # swap numbers x and y using tuple unpacking
print("x =", x)
print("y =", y)

# use extra variables
x = 10 # first number
y = 20 # second number
temp = x # store value of x in temp
x = y # store value of y in x
y = temp # store value of temp in y
print("x =", x)
print("y =", y)

# find the largest number
x = 10 # first number
y = 20 # second number
z = 30 # third number
if x > y and x > z:
    print("x is the largest number")
elif y > x and y > z:
    print("y is the largest number")
else:
    print("z is the largest number")


