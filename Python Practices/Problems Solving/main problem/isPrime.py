def Is_Prime(n):
    if n <= 1 or n == 0:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

n = int(input("Enter a number: "))
for i in range(2, n):
    if Is_Prime(i):
        print(f'{i} is a prime number')
    else:
        print(f'{i} is not a prime number')