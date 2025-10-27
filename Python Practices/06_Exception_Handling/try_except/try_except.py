# ============================= What is Try Except =============================
# try-except is Python-of error handling system।
# where error in try block, then except block will be executed.
# where no error in try block, then except block will not be executed.
# Structure:
# try:
#     # try block
# except:
#     # except block


# ============================= basic try except =============================
# Simple example of try except
try:
    x = int(input("Enter a number: "))
    result = 10 / x
    print("Result:", result)
except:  # noqa: E722
    print("Something went wrong!")

try:
    x = int(input("Enter a number: "))
    result = 10 / x
    print("Result:", result)
except Exception as e:
    print("Something went wrong!", e)


# ============================= try except =============================
# How to use try except with specific errors5


try:
    x = int(input("Enter a number: "))
    result = 10 / x
except ValueError:
    print("Please enter a valid number!")
except ZeroDivisionError:
    print("You cannot divide by zero!")


# ============================= practical use cases =========================
# - Data processing
# - Business logic
# - Algorithm implementation

# Example 1: Data processing
try:
    with open("data.txt") as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print("File not found!")

# Example 2: Business logic (API, payment, etc.)
try:
    print("Processing payment...")
    # imaginary_payment_gateway.process()
except Exception as e:
    print("Payment failed:", e)

# Example 3: Algorithm implementation
try:
    numbers = [10, 5, 0, 2]
    for n in numbers:
        print(10 / n)
except ZeroDivisionError:
    print("Skipped division by zero")
