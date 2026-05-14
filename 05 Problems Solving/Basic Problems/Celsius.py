# Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius
    Formula: (F - 32) * 5/9
    100 - 32 = 68 
    68 * 5 = 340
    340 / 9 = 37.78
    """
    return (fahrenheit - 32) * 5/9

# Test the function
print(fahrenheit_to_celsius(90))  # Expected: 32.22
print(fahrenheit_to_celsius(100))  # Expected: 37.78