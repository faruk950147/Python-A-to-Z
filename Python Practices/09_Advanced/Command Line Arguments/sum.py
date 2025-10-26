# filename: calculator.py
import sys

# Check if enough arguments are provided
if len(sys.argv) != 3:
    print("Usage: python calculator.py <num1> <num2>")
    sys.exit(1)

# Get command line arguments
num1 = sys.argv[1]
num2 = sys.argv[2]

# Convert strings to numbers
try:
    num1 = float(num1)
    num2 = float(num2)
except ValueError:
    print("Please provide valid numbers.")
    sys.exit(1)

# Perform addition
result = num1 + num2

# Print result
print(f"The sum of {num1} and {num2} is {result}")

# ============================== run ============================== #
# python calculator.py 10 20

# Check if enough arguments are provided
if len(sys.argv) != 4:
    print("Usage: python calculator.py <num1> <operator> <num2>")
    print("Operators: +, -, *, /")
    sys.exit(1)

# Get command line arguments
num1 = sys.argv[1]
operator = sys.argv[2]
num2 = sys.argv[3]

# Convert strings to numbers
try:
    num1 = float(num1)
    num2 = float(num2)
except ValueError:
    print("Please provide valid numbers.")
    sys.exit(1)

# Perform calculation
if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
        sys.exit(1)
    result = num1 / num2
else:
    print("Invalid operator! Use one of: +, -, *, /")
    sys.exit(1)

# Print result
print(f"{num1} {operator} {num2} = {result}")

# ============================== run ============================== #
# python calculator.py 10 + 20
