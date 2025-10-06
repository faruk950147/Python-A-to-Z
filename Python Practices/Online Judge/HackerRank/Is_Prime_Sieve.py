def Is_Prime_Sieve(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif (n % 2) == 0 or (n % 3) == 0:
        return False
    else:
        i = 5
        while (i * i <= n):
            if (n % i) == 0 or (n % (i + 2)) == 0:
                return False
            i += 6
    return True

n = int(input())
for x in range(1, n):
    if Is_Prime_Sieve(x):
        print(f'{x} is a prime number')
    else:
        print(f'{x} is not a prime number')