def sum(n):
    if n == 1 or n == 0: # Base case
        return n
    return n + sum(n-1) # Recursive case

print(sum(5))