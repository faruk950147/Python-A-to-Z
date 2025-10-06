def fib(n):
    if n == 0 or n == 1: # Base case
        return n
    return fib(n-1) + fib(n-2) # Recursive case

print(fib(6))