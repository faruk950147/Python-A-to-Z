# eval() is a built-in function that evaluates a string as a Python expression.
# takes three arguments: expression, globals, and locals.
# globals is a dictionary of global variables.
# locals is a dictionary of local variables.
# string is the string to be evaluated.
# return the result of the expression.

# Example
# syntax of eval is: eval(expression, globals=None, locals=None)
# print(eval('x + 1', {'x': 1}, {'x': 2}))
x = 10
print(eval('x + 1'))