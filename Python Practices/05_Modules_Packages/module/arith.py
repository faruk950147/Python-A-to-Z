from logger import log_info, log_error
import math

class Mathematics:
    def __init__(self):
        pass

    def addition(self, *args):
        try:
            if not args:
                return 0
            total = sum(args)
            log_info(f"Addition successful: {list(args)} = {total}")
            return total
        except Exception as e:
            log_error(f"Error calculating sum: {e}")
            return None

    def difference(self, *args):
        try:
            if not args:
                return 0
            result = args[0]
            for num in args[1:]:
                result -= num
            log_info(f"Difference successful: {list(args)} = {result}")
            return result
        except Exception as e:
            log_error(f"Error calculating difference: {e}")
            return None

    def multiplication(self, *args):
        try:
            if not args:
                return 1
            result = 1
            for num in args:
                result *= num
            log_info(f"Multiplication successful: {list(args)} = {result}")
            return result
        except Exception as e:
            log_error(f"Error calculating multiplication: {e}")
            return None

    def division(self, *args):
        try:
            if not args:
                return None
            result = args[0]
            for num in args[1:]:
                if num == 0:
                    raise ZeroDivisionError("Cannot divide by zero.")
                result /= num
            log_info(f"Division successful: {list(args)} = {result}")
            return result
        except Exception as e:
            log_error(f"Error calculating division: {e}")
            return None

    def power(self, *args):
        try:
            if not args:
                return None
            result = args[0]
            for num in args[1:]:
                result **= num
            log_info(f"Power successful: {list(args)} = {result}")
            return result
        except Exception as e:
            log_error(f"Error calculating power: {e}")
            return None

    def square_root(self, *args):
        try:
            results = []
            for num in args:
                if num < 0:
                    raise ValueError("Cannot take square root of negative number.")
                results.append(math.sqrt(num))
            log_info(f"Square roots calculated: {results}")
            return results
        except Exception as e:
            log_error(f"Error calculating square root: {e}")
            return None

    def cube_root(self, *args):
        try:
            results = []
            for num in args:
                results.append(num ** (1/3))
            log_info(f"Cube roots calculated: {results}")
            return results
        except Exception as e:
            log_error(f"Error calculating cube root: {e}")
            return None

    def factorial(self, *args):
        try:
            results = []
            for num in args:
                if not isinstance(num, int) or num < 0:
                    raise ValueError("Factorial can only be calculated for non-negative integers.")
                results.append(math.factorial(num))
            log_info(f"Factorials calculated: {results}")
            return results
        except Exception as e:
            log_error(f"Error calculating factorial: {e}")
            return None

    def absolute_value(self, *args):
        try:
            results = [abs(num) for num in args]
            log_info(f"Absolute values calculated: {results}")
            return results
        except Exception as e:
            log_error(f"Error calculating absolute value: {e}")
            return None

if __name__ == "__main__":
    mathematics = Mathematics()
    mathematics.addition(10,90)