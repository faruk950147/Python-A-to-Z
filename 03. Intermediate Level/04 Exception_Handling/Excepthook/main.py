# ============================= what is exception handling =============================
# Exception handling is a mechanism in Python to handle runtime errors.
# It allows the program to continue running even if an error occurs.


# ============================= what is except hook =============================
# Exception hook (sys.excepthook) is a global exception handler in Python.
# It is a function that is automatically called when an exception is not handled.
# By default, it prints the traceback and stops the program.


# ============================= why need except hook =============================
# Exception hook is used to handle unhandled exceptions globally.
# It helps to:
#   - Log errors into a file
#   - Show custom error messages
#   - Gracefully shut down the program without a crash


# ============================= working flow of except hook =============================
# 1. An exception occurs.
# 2. Python checks if the exception is handled with try-except.
# 3. If not handled, Python calls sys.excepthook(type, value, traceback).
# 4. You can override sys.excepthook to customize the behavior.


# ============================= example =============================
import sys

# Custom exception hook
def custom_excepthook(exc_type, exc_value, exc_traceback):
    print("Unhandled Exception Detected!")
    print("Type:", exc_type.__name__)
    print("Message:", exc_value)
    print("Program closing safely...")

# Replace default excepthook with custom one
sys.excepthook = custom_excepthook

# Generate an unhandled exception
print(10 / 0)
