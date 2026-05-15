class TemperatureConverter:
    """
    A class to convert temperatures between Fahrenheit and Celsius.
    """
    def __init__(self):
        pass
    
    def fahrenheit_to_celsius(self, fahrenheit):
        """
            Convert Fahrenheit to Celsius
            Formula: (F - 32) * 5/9
            100 - 32 = 68 
            68 * 5 = 340
            340 / 9 = 37.78
        """
        return round((fahrenheit - 32) * 5/9, 2)
    
    def celsius_to_fahrenheit(self, celsius):
        """
            Convert Celsius to Fahrenheit
            Formula: (C * 9/5) + 32
            30 * 9/5 = 54
            54 + 32 = 86
        """
        return round((celsius * 9/5) + 32, 2)

# Test the class

if __name__ == "__main__":
    converter = TemperatureConverter()
    print(converter.fahrenheit_to_celsius(90.00))  # Expected: 32.22
    print(converter.celsius_to_fahrenheit(32.22))  # Expected: 89.6
