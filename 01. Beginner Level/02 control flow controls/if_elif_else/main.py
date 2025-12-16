"""
You think your father three son that mean one father of three son.
# if condition:
    # The if statement evaluates a condition (an expression that results in True or False). 
    # If the condition is true, the code block inside the if statement is executed. 
    # If the condition is false, the code block is skipped.
    # "if condition is true?"

# elif condition:
    # The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".
    # The elif keyword allows you to check multiple expressions for True and execute a block of code as soon as one of the conditions evaluates to True.
    # "elif condition is true?"

# else:
    # The else keyword is Python's way of saying "if none of the previous conditions were true, then try this condition".
    # The else keyword is optional and is used to execute a block of code when none of the previous conditions are true.
    # "else condition is true?"
    #
"""


a = 10
b = 20

if a > b:
    print(f"{a} is greater than {b}")
else:
    print(f"{b} is greater than {a}")

if a < b:
    print(f"{a} is less than {b}")
else:
    print(f"{a} is greater than {b}")