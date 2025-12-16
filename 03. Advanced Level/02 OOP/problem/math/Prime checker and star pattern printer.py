# class PrimeChecker:
#     def __init__(self, number):
#         self.number = number

#     def is_prime(self):
#         """Check if the number is prime"""
#         if self.number < 2:
#             return False
#         for i in range(2, int(self.number ** 0.5) + 1):
#             if self.number % i == 0:
#                 return False
#         return True


# if __name__ == "__main__":
#     try:
#         num = int(input("Enter a number to check if it's prime: "))
#         checker = PrimeChecker(num)
#         if checker.is_prime():
#             print(f"{num} is a Prime Number.")
#         else:
#             print(f"{num} is NOT a Prime Number.")
#     except ValueError:
#         print("Please enter a valid integer.")
        
        
        
class StarPattern:
    def __init__(self, rows):
        self.rows = rows

    def pyramid(self):
        """Pyramid Pattern"""
        print("\nPyramid Pattern\n")
        for i in range(1, self.rows + 1):
            print(" " * (self.rows - i) + "* " * i)

    def inverted_pyramid(self):
        """Inverted Pyramid Pattern"""
        print("\nInverted Pyramid Pattern\n")
        for i in range(self.rows, 0, -1):
            print(" " * (self.rows - i) + "* " * i)

    def diamond(self):
        """Diamond Pattern"""
        print("\nDiamond Pattern\n")
        # Upper part
        for i in range(1, self.rows + 1):
            print(" " * (self.rows - i) + "* " * i)
        # Lower part
        for i in range(self.rows - 1, 0, -1):
            print(" " * (self.rows - i) + "* " * i)


if __name__ == "__main__":
    try:
        rows = int(input("Enter number of rows for pattern: "))
        pattern = StarPattern(rows)
        pattern.pyramid()
        pattern.inverted_pyramid()
        pattern.diamond()

    except ValueError:
        print("Please enter a valid integer.")
       

