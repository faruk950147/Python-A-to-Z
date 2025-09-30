def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))

def fibonacci_iterative(n):
    a, b = 0, 1
    sequence = []
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

print(fibonacci_iterative(10))


def fibonacci_no_list(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")   
        a, b = b, a + b

fibonacci_no_list(10)
