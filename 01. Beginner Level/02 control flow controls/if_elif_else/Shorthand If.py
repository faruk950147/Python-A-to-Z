# Python Shorthand If
# Short Hand If
# If you have only one statement to execute, you can put it on the same line as the if statement.

# ExampleGet your own Python Server
# One-line if statement:

a = 5
b = 2
if a > b: print("a is greater than b")

# Note: You still need the colon : after the condition.

# Short Hand If ... Else
# If you have one statement for if and one for else, you can put them on the same line using a conditional expression:

# Example
# One-line if/else that prints a value:

a = 2   
b = 330
print("A") if a > b else print("B")

# This is called a conditional expression (sometimes known as a "ternary operator").

# Assign a Value With If ... Else
# You can also use a one-line if/else to choose a value and assign it to a variable:

# Example
a = 10
b = 20
bigger = a if a > b else b
print("Bigger is", bigger)

# The syntax follows this pattern:

# variable = value_if_true if condition else value_if_false
# Multiple Conditions on One Line
# You can chain conditional expressions, but keep it short so it stays readable:

# Example
# One line, three outcomes:

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

# Practical Examples
# Ternary operators are particularly useful for simple assignments and return statements.

# Example
# Finding the maximum of two numbers:

x = 15
y = 20
max_value = x if x > y else y
print("Maximum value:", max_value)
# Example
# Setting a default value:

username = ""
display_name = username if username else "Guest"
print("Welcome,", display_name)
# When to Use Shorthand If
# Shorthand if statements and ternary operators should be used when:

# The condition and actions are simple
# It improves code readability
# You want to make a quick assignment based on a condition
# Important: While shorthand if statements can make code more concise, 
# avoid overusing them for complex conditions. For readability, 
# use regular if-else statements when dealing with multiple lines of code or complex logic.