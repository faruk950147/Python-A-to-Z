
'''
Python closure কখনোই class-based না। এটা পুরোপুরি function-based concept।
Closure কী?
Simple Closure Example
def calculator(n):    def add(x):        return x + n   # n remembers (closure)    return addadd5 = calculator(5)print(add5(10))  # 15
Here add() function remembers n -> this is closure

Closure why not class?
Reasons:

Closure = function + lexical scope memory

Class = object + attributes + methods

Two different concepts

Class with same behaviour (but NOT closure)
class Calculator:    def __init__(self, n):        self.n = n    def add(self, x):        return x + self.ncalc = Calculator(5)print(calc.add(10))  # 15
This is not closure
This is OOP (class-based state)

Key Difference
ClosureClassFunction-basedOOP-basedouter variable remembersself attribute storeslightweightheavier structureno object neededobject create

Final Answer
Python closure = function-based concept
Class-based closure doesn't exist (but class can mimic same behaviour)
'''
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

add_10 = outer_function(10)

print(add_10(5))            # Output: 15
print(add_10.__closure__)   # Check closure info
print(add_10.__closure__[0].cell_contents) # Check closure value details

# Class-based approach same behavior but not closure
class Calculator:
    def __init__(self, n):
        self.n = n
    def add(self, x):
        return x + self.n

calc = Calculator(5).add
print(calc(10))  # 15
print(calc.__closure__)   # Check closure (None for class-based)