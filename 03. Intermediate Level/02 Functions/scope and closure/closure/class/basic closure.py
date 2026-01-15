class Calculations:
    def __init__(self, n):
        self.n = n  # Stored value for calculations

    def multiply(self, x):
        return x * self.n

    def add(self, x):
        return x + self.n

    def subtract(self, x):
        return x - self.n

    def divide(self, x):
        if self.n == 0:
            raise ValueError("Cannot divide by zero!")
        return x / self.n

    def power(self, x):
        return x ** self.n


# --- Example usage ---
calc = Calculations(3)

print(calc.multiply(5))  # 15
print(calc.add(5))       # 8
print(calc.subtract(5))  # 2
print(calc.divide(9))    # 3.0
print(calc.power(2))     # 8
print(calc.__dict__)     # {'n': 3}

