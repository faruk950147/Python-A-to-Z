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
        return (fahrenheit - 32) * 5/9
    
    def celsius_to_fahrenheit(self, celsius):
        """
            Convert Celsius to Fahrenheit
            Formula: (C * 9/5) + 32
            0 * 9/5 = 0
            0 + 32 = 32
        """
        return (celsius * 9/5) + 32

# Test the class

if __name__ == "__main__":
    converter = TemperatureConverter()
    print(converter.fahrenheit_to_celsius(90))  # Expected: 32.22
    print(converter.fahrenheit_to_celsius(100))  # Expected: 37.78
    print(converter.celsius_to_fahrenheit(0))  # Expected: 32.0
    print(converter.celsius_to_fahrenheit(100))  # Expected: 212.0