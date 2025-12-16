# ============================= What is Pure Function =============================
# A Pure Function is a function that always produces the same output 
# for the same input and does not cause any side effects.


# ============================= basic pure function =============================
# Example 1: Pure Function
def add(a, b):
    return a + b

print(add(2, 3))  # Output: 5
print(add(2, 3))  # Output: 5 (same input -> same output)

# Example 2: Pure Function
def square(x):
    return x * x

print(square(4))  # Output: 16
print(square(4))  # Output: 16


# ============================= side effects =============================
# Side effects mean the function modifies external state or interacts 
# with the outside world (e.g., global variables, I/O, print, DB update).

# Example: Impure Function (with side effect)
result = 0
def add_with_side_effect(a, b):
    global result
    result = a + b    # modifies global variable (side effect)
    print(result)     # printing output (side effect)
    return result

add_with_side_effect(2, 3)  # Output: 5
print(result)  # external variable changed


# ============================= pure function vs impure function =============================
# Pure Function:
# - Always returns the same output for the same input.
# - Does not modify external data or state.
# - Easy to test, debug, and optimize.

# Impure Function:
# - May return different results for the same input (depends on external state).
# - Can modify global variables, perform I/O, etc.
# - Harder to debug and test.

# Example: Impure Function
import random
def get_random_number():   # impure (because it gives different output each time)
    return random.randint(1, 10)


# ============================= pure function optimization =============================
# Pure functions are easy to optimize because the output is predictable.
# Technique: Memoization (cache previously computed results).

# Example: Fibonacci with memoization
cache = {}
def fib(n):
    if n in cache:   # return from cache if already computed
        return cache[n]
    if n <= 1:
        cache[n] = n
    else:
        cache[n] = fib(n-1) + fib(n-2)
    return cache[n]

print(fib(10))  # Output: 55


# ============================= practical use cases =============================
# Pure functions are very useful in:
# - Data processing (map, filter, reduce)
# - Business logic (e.g., discount calculation)
# - Algorithm implementation (recursion, sorting, searching)
# - Functional programming

# Example: Data Processing with map
nums = [1, 2, 3, 4, 5]
squared = list(map(square, nums))  # map with pure function
print(squared)  # Output: [1, 4, 9, 16, 25]
