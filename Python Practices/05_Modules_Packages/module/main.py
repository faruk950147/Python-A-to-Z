# main.py
from logger_module import log_info, log_error

def calculate_sum(numbers):
    try:
        total = sum(numbers)
        log_info(f"Sum calculated successfully: {total}")
        return total
    except Exception as e:
        log_error(f"Error calculating sum: {e}")
        return None


# Test the function
nums = [10, 20, 30, 40]
print("Total:", calculate_sum(nums))
