class Multiplier:
    def __init__(self, n):
        self.n = n

    def multiply(self, x):
        return x * self.n

double = Multiplier(2)

print(double.multiply(5))  # 10
print(double.__dict__)     # Check stored data
