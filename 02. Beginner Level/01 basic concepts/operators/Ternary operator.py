# ======================= Ternary operator =======================

# Ternary operator in python does not exist but we can use it by using if-else
# Ternary operators is a symbol that is used to perform ternary operations.

# condition_if_true if condition else condition_if_false

# The syntax for Python’s ternary operator (one-line if-else) is:

# result = value_if_true if condition else value_if_false

books = ["Python", "Django", "Flask", "FastAPI", "React"]

first_book = books[0] if books else None
print(first_book)  # Output: Python