def fact(n):
    if n == 1 or n == 0: # Base case
        return 1
    return n * fact(n-1) # Recursive case

print(fact(5))  