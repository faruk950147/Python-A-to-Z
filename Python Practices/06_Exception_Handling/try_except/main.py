# ============================= What is Try Except =============================
# try-except is Python-of error handling system।
# where error in try block, then except block will be executed.
# where no error in try block, then except block will not be executed.
# Structure:
# try:
#     # try block
# except Exception as e:
#     # except block

# ============================== 1. math try except =============================
import os
try:
    num1, num2 = list(map(int, input('Enter two numbers: ').split()))
    print(num1 + num2)
except Exception as e:
    print("Invalid input", str(e))
    
try:
    num1, num2 = list(map(int, input('Enter two numbers: ').split()))
    print(num1 / num2)
except ZeroDivisionError:
    print("Cannot divide by zero.")
except Exception as e:
    print("Invalid input", str(e))
    
# ============================== 3. file try except =============================

try:
    if os.path.exists('data.txt'):
        with open('data.txt', 'r') as file:
            print(file.read())
    else:
        with open('data.txt', 'w') as file:
            file.write('Hello World')
except Exception as e:
    print("An error occurred:", str(e))

    
# ============================== 2. function try except =============================
def add_numbers(a, b):
    return a + b

try:
    num1, num2 = map(int, input('Enter two numbers: ').split())
    print("Sum from input:", add_numbers(num1, num2))
except ValueError:
    print("Invalid input. Please enter exactly two integers.")

print("Sum from function:", add_numbers(1, 2))

def divide_numbers(a, b):
    return a / b

try:
    num1, num2 = map(int, input('Enter two numbers: ').split())
    print("Division from input:", divide_numbers(num1, num2))
except ValueError:
    print("Invalid input. Please enter exactly two integers.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
except Exception as e:
    print("An error occurred:", str(e))






