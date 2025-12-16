# ============================= What is Finally Else =============================
# 'finally' is used to execute code that should run regardless of whether an exception occurred or not.
# 'else' is used to execute code that should run only if no exception occurred.

# Structure:
# try:
#     # code that may raise an exception
# except ExceptionType:
#     # code to handle the exception
# else:
#     # code to run if no exception occurred
# finally:
#     # code to run regardless of whether an exception occurred or not

# ============================== 1. math finally else =============================
import os

try:
    num1, num2 = map(int, input('Enter two numbers: ').split())
    print("Sum from input:", num1 + num2)
except ValueError:
    print("Invalid input. Please enter exactly two integers.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
except Exception as e:
    print("An error occurred:", str(e))
else:
    print("No exceptions occurred.")
finally:
    print("This will always run.")


# ============================== 2. file finally else =============================
try:
    if os.path.exists('data.txt'):
        with open('data.txt', 'r') as file:
            print(file.read())
    else:
        with open('data.txt', 'w') as file:
            file.write('Hello World')
except Exception as e:
    print("An error occurred:", str(e))
else:
    print("No exceptions occurred.")
finally:
    print("This will always run.")
    
# ============================== 3. function finally else =============================
def add_numbers(a, b):
    return a + b

try:
    num1, num2 = map(int, input('Enter two numbers: ').split())
    print("Sum from function:", add_numbers(num1, num2))
except ValueError:
    print("Invalid input. Please enter exactly two integers.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
except Exception as e:
    print("An error occurred:", str(e))
else:
    print("No exceptions occurred.")
finally:
    print("This will always run.")
    
# ============================== 4. class finally else =============================
class Calculator:
    def add(self, a, b):
        return a + b
    
def divide(self, a, b):
    return a / b
if __name__ == "__main__":
    try:
        calc = Calculator()
        num1, num2 = map(int, input('Enter two numbers: ').split())
        print("Sum from input:", calc.add(num1, num2))
    except ValueError:
        print("Invalid input. Please enter exactly two integers.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    except Exception as e:
        print("An error occurred:", str(e))
    else:
        print("No exceptions occurred.")
    finally:
        print("This will always run.")
