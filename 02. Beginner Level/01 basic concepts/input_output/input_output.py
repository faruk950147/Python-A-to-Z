# input function get input from user
# output function print output to user

# input function
# input function get input from user it's get one input return string
name = input("Enter your name: ") 

# output function
print("Hello", name)


# input function
# input function get input from user it's get one input return integer
age = int(input("Enter your age: ")) 

# output function
print("Hello", name, "you are", age, "years old")


# multiple input function in one line
# input function get input from user it's get two input 
# return string and convert to integer
x, y = input("Enter two numbers: ").split() # split() function split string into list
x = int(x)
y = int(y)
print("x + y =", x + y)

# map is a higher-order function that applies a given function to each item of an iterable (list, tuple etc.)
# and returns a list of the results

# multiple input function in one line
# input function get input from user it's get two input 
# return string and convert to integer
m, n = map(int, input("Enter two numbers: ").split()) 
print("m + n =", m + n)

# multiple input function in one line
# input function get input from user it's get two input 
# return string and convert to integer
a, b = list(map(int, input().split())) 
print("a + b =", a + b)