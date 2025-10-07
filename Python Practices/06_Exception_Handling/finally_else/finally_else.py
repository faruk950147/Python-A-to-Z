# ============================= What is Finally Else =============================
# finally and else are additional parts of a try-except block.
# finally: contains code that should always run, no matter what (e.g., closing files).
# else: contains code that runs only if no exception occurs in the try block.

# Structure:
# try:
#     # code that might raise an error
# except:
#     # code that runs if an error occurs
# else:
#     # code that runs only if try has no error
# finally:
#     # code that always runs at the end


# ============================= basic finally else =============================
# Simple example of finally

try:
    x = int(input("Enter a number: "))
    result = 10 / x
    print("Result:", result)
except:  # noqa: E722
    print("Something went wrong!")
finally:
    print("Finally block is always executed.")


# ============================= finally else =============================
# How to use finally and else together

try:
    x = int(input("Enter a number: "))
    result = 10 / x
    print("Result:", result)
except:  # noqa: E722
    print("Something went wrong!")
else:
    print("Else block is executed when try block does not raise an exception.")
finally:
    print("Finally block is always executed.")


# ============================= practical use cases =============================
# - Data processing (close files or release resources)
# - Business logic (commit or rollback transactions)
# - Algorithm implementation (cleanup operations)

# Example 1: Data processing
try:
    f = open("data.txt", "r")
    content = f.read()
    print(content)
except FileNotFoundError:
    print("File not found!")
else:
    print("File read successfully!")
finally:
    print("File closed (even if error occurred).")
    try:
        f.close()
    except:  # noqa: E722
        pass

# Example 2: Business logic
try:
    print("Processing payment...")
    # imaginary_payment_gateway.process()
except Exception as e:
    print("Payment failed:", e)
else:
    print("Payment successful!")
finally:
    print("Transaction completed (logged).")
