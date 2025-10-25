# ====================== What is Argument ======================
# An argument is a value that is passed to a function when it is called.
# These values are assigned to the function’s parameters.

# Example:
def greet(name):
    return f"Hello, {name}!"

print(greet("Faruk"))   # Output: Hello, Faruk!


# ====================== Types of Arguments ======================
# 1. Positional Arguments
# 2. Keyword Arguments
# 3. Default Arguments
# 4. Mutable Immutable Default Arguments
# 5. Variable-Length Arguments (*args)
# 6. Keyword Variable-Length Arguments (**kwargs)
# 7. Combination of All Types


# ===============================================================
# 1. Positional Arguments
# ---------------------------------------------------------------
# Positional arguments are passed to a function in the same order
# as the parameters are defined.
# The order is VERY important for positional arguments.
# ===============================================================

def display(name, age):
    return f"Name: {name}, Age: {age}"

# Correct: order matches parameter order
print(display("John", 25))   

# Incorrect: order is wrong (age, name)
print(display(25, "John"))   


# ===============================================================
# 2. Keyword Arguments
# ---------------------------------------------------------------
# Keyword arguments are passed using parameter names.
# The order does not matter when using keyword arguments.
# ===============================================================

def display(name, age):
    return f"Name: {name}, Age: {age}"

# Both correct (order doesn’t matter)
print(display(name="John", age=25))
print(display(age=25, name="John"))


# ===============================================================
# 3. Default Arguments
# ---------------------------------------------------------------
# Default arguments have a predefined value.
# If no value is provided, the default one is used.
# It's recommended to use immutable types (int, str, tuple) as defaults.
# Avoid using mutable types (list, dict) as default values.
# ========================== Immutable Default Arguments =========================

def display(name, age=18):
    return f"Name: {name}, Age: {age}"

# Uses default age value = 18
print(display("John"))          # Output: Name: John, Age: 18

# Overrides default age
print(display("Alice", 25))     # Output: Name: Alice, Age: 25


# ===============================================================
# 4. Mutable Default Arguments
# ---------------------------------------------------------------
# Bad practice (mutable default)
# def add_info(name, employee_data=[]):
#     employee_data.append(name)
#     return employee_data
# # Every call shares the same list!

# Correct way (use None as default)
def add_info(name, employee_data=None):
    if employee_data is None:
        employee_data = []
    employee_data.append(name)
    return employee_data

print(add_info("John"))   # ['John']
print(add_info("Alice"))  # ['Alice']


# ===============================================================
# 5. Variable-Length Arguments (*args)
# ---------------------------------------------------------------
# When you don’t know how many positional arguments will be passed,
# use *args. It collects all positional arguments as a tuple.
# ===============================================================

def add(*numbers):
    total = 0
    for n in numbers:
        total += n
    return f"Sum: {total}"

# Any number of arguments can be passed
print(add(10, 20))               # Output: Sum: 30
print(add(10, 20, 30, 40))       # Output: Sum: 100


# ===============================================================
# 6. Keyword Variable-Length Arguments (**kwargs)
# ---------------------------------------------------------------
# When you don’t know how many keyword arguments will be passed,
# use **kwargs. It collects them as a dictionary.
# ===============================================================

def info(**data):
    for key, value in data.items():
        print(f"{key}: {value}")

info(name="John", age=25, country="USA")

# OR return the whole dictionary
def info_dict(**data):
    return data

print(info_dict(name="John", age=25, country="USA"))
# Output:
# {'name': 'John', 'age': 25, 'country': 'USA'}


# ===============================================================
# 7. Combination of All Types
# ---------------------------------------------------------------
# You can combine positional, keyword, default, *args, and **kwargs
# in one function.
# ===============================================================

def full_info(id, name, age=18, *skills, **details):
    print(f"ID: {id}")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Skills: {skills}")
    print(f"Other Details: {details}")

full_info(
    101,
    "Faruk",
    22,
    "Python", "Django", "Kotlin",
    country="Bangladesh",
    profession="Programmer"
)

# Output:
# ID: 101
# Name: Faruk
# Age: 22
# Skills: ('Python', 'Django', 'Kotlin')
# Other Details: {'country': 'Bangladesh', 'profession': 'Programmer'}


# ===============================================================
# ====================== Summary ================================
# ===============================================================

# | Type | Syntax | Description | Example |
# |------|---------|-------------|----------|
# | Positional | normal order | order matters | display("John", 25) |
# | Keyword | name=value | order doesn’t matter | display(age=25, name="John") |
# | Default | param=value | default value used if not given | def f(x=10): |
# | Variable-Length | *args | collects all positional arguments | add(10,20,30) |
# | Keyword Variable-Length | **kwargs | collects all keyword arguments | info(name="John", age=25) |
