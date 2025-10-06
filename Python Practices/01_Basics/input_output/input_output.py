# input function get input from user
# output function print output to user

# input function
name = input("Enter your name: ")

# output function
print("Hello", name)


# input function
age = int(input("Enter your age: "))

# output function
print("Hello", name, "you are", age, "years old")


# multiple input function in one line
x, y = input("Enter two numbers: ").split()
x = int(x)
y = int(y)
print("x + y =", x + y)

# multiple input function in one line
m, n = map(int, input("Enter two numbers: ").split())
print("m + n =", m + n)