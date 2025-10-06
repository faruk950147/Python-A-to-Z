def Is_Prime(n):
    if n <= 1 or n == 0:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

n = int(input("Enter a number: "))
if Is_Prime(n):
    print(f'{n} is a prime number')
else:
    print(f'{n} is not a prime number')
