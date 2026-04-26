# ======================= Ternary operator =======================

# Ternary operator in python does not exist but we can use it by using if-else
# Ternary operators is a symbol that is used to perform ternary operations.

# # Syntax:
# value_if_true if condition else value_if_false


books = ["Python", "Django", "Flask", "FastAPI", "React"]

first_book = books[0] if books else None
print(first_book)  # Output: Python