# ====================== what is assert ======================
# assert is a keyword in Python
# ====================== syntax =============================
# assert condition
# assert condition, message
# ====================== usage ============================
# assert is used to testing and debugging mainly used in development 
# but not used in production
# assert is used to check preconditions of a function if the condition is false it will raise an AssertionError
# ====================== procedure ============================
# 1. assert condition
# 2. assert condition, message
try:
    age = float(input("Enter your age: "))
    assert age >= 18, "Age must be at least 18"
except AssertionError as e:
    print(e)
except ValueError as e:
    print(e)

# ====================== function ============================
def validate_age(age):
    assert age >= 18, "Age must be at least 18"
    print("Age is valid")

try:
    age = float(input("Enter your age: "))
    validate_age(age)
except AssertionError as e:
    print(e)