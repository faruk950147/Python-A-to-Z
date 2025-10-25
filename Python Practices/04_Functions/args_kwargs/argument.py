# ====================== What is Argument ======================
# An argument is a value that is passed to a function when it is called.
# These values are assigned to the function’s parameters.

# ====================== Types of Arguments ======================

# 1. Positional Arguments
# ---------------------------------------------------------------
# Positional arguments are passed to a function in the same order
# as the parameters are defined. The order is important.
# Order is very important for positional arguments.
def display(name, age):
    return name, age

print(display(f"Positional Arguments Name: {"John"}, Age: {25}"))   # Correct
print(display(f"Positional Arguments Age: {25}, Name: {"John"}"))   # Incorrect (order is wrong)


# 2. Keyword Arguments
# ---------------------------------------------------------------
# Keyword arguments are passed with parameter names
# Order is not important for keyword arguments.

def display(name, age):
    return name, age

print(display(f"Keyword Arguments Name: {"John"}, Age: {25}"))  # Correct
print(display(f"Keyword Arguments Age: {25}, Name: {"John"}"))  # Also correct (order doesn’t matter)


# 3. Default Arguments
# ---------------------------------------------------------------
# Default arguments have a predefined value.
# If no value is provided, the default one is used.

def display(name, age=18):
    return name, age

print(display(f"Default Arguments Name: {"John"}, Age: {25}"))        # Output: Name: John Age: 18
print(display(f"Default Arguments Name: {"Alice"}, Age: {25}"))   # Output: Name: Alice Age: 25


# 4. Variable-Length Arguments (*args)
# ---------------------------------------------------------------
# When you don’t know how many arguments will be passed,
# use *args. It collects all positional arguments as a tuple.

def add(*numbers):
    total = 0
    for n in numbers:
        total += n
    return "Sum: ", total

print(add(f"Variable-Length Arguments: {10, 20}"))          # Output: Sum: 30
print(add(f"Variable-Length Arguments: {10, 20, 30, 40}"))  # Output: Sum: 100


# 5. Keyword Variable-Length Arguments (**kwargs)
# ---------------------------------------------------------------
# When you don’t know how many keyword arguments will be passed,
# use **kwargs. It collects them as a dictionary.

def info(**data):
    for key, value in data.items():
        return key, ":", value

print(info(name="John", age=25, country="USA"))

# Output:
# name : John
# age : 25
# country : USA

def info(**data):
    return data

print(info(name="John", age=25, country="USA"))
# Output:
# name : John
# age : 25
# country : USA


# ====================== Summary ======================

# | Type | Syntax | Description | Example |
# |------|---------|--------------|----------|
# | Positional | normal order | order matters | display("John", 25) |
# | Keyword | name=value | order doesn’t matter | display(age=25, name="John") |
# | Default | param=value | default value used if not given | def f(x=10): |
# | Variable-Length | *args | collects all positional arguments | add(10,20,30) |
# | Keyword Variable-Length | **kwargs | collects all keyword arguments | info(name="John", age=25) |
