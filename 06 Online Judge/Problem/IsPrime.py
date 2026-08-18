

class IsPrime:

    def is_prime(self, n):
        """Check if a number is prime"""

        if n < 2:
            return False

        for i in range(2, int(n ** 0.5) + 1):

            if n % i == 0:
                return False

        return True


# --- Program Run ---

prime_checker = IsPrime()

num = int(input("Enter a number to check if it's prime: "))

if prime_checker.is_prime(num):
    print(f"{num} is a Prime Number.")
else:
    print(f"{num} is NOT a Prime Number.")