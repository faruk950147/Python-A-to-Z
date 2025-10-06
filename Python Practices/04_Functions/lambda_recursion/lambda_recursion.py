# ============================= What is Lambda Recursion =============================
# Recursion means a function calling itself to solve a problem.
# With lambda, recursion is possible but less common in Python, 
# because lambda is anonymous and has only one expression.


# ============================= basic lambda recursion =============================
# Example: Normal recursive function (not lambda)
def countdown(n):
    if n == 0:
        return "Done"
    return f"{n}, " + countdown(n - 1)

print(countdown(5))  # Output: 5, 4, 3, 2, 1, Done

# Example: Lambda recursion using assignment
fact = (lambda f: (lambda n: 1 if n == 0 else n * f(f)(n - 1)))(
    lambda f: (lambda n: 1 if n == 0 else n * f(f)(n - 1))
)
print(fact(5))  # Output: 120


# ============================= factorial using lambda recursion =====================
# Factorial: n! = n * (n-1) * (n-2) * ... * 1

factorial = (lambda f: (lambda n: 1 if n == 0 else n * f(f)(n - 1)))(
    lambda f: (lambda n: 1 if n == 0 else n * f(f)(n - 1))
)
print(factorial(6))  # Output: 720


# ============================= fibonacci using lambda recursion =====================
# Fibonacci: F(n) = F(n-1) + F(n-2), with base F(0)=0, F(1)=1

fibonacci = (lambda f: (lambda n: n if n <= 1 else f(f)(n - 1) + f(f)(n - 2)))(
    lambda f: (lambda n: n if n <= 1 else f(f)(n - 1) + f(f)(n - 2))
)
print(fibonacci(7))  # Output: 13


# ============================= tail lambda recursion ===============================
# Tail recursion means the recursive call is the LAST action in the function.
# Example with normal function:
def tail_fact(n, acc=1):
    if n == 0:
        return acc
    return tail_fact(n - 1, acc * n)

print(tail_fact(5))  # Output: 120

# With lambda (harder but possible):
tail_factorial = (lambda f: (lambda n, acc=1: acc if n == 0 else f(f)(n - 1, acc * n)))(
    lambda f: (lambda n, acc=1: acc if n == 0 else f(f)(n - 1, acc * n))
)
print(tail_factorial(5))  # Output: 120


# ============================= tail lambda recursion vs normal recursion ===========
# Normal recursion:
# - Function performs extra operations after recursive call.
# - Example: return n * factorial(n-1)
#
# Tail recursion:
# - Recursive call is the last operation (no extra work after return).
# - Optimized by reusing stack frames in some languages (not in Python).


# ============================= tail lambda recursion optimization =================
# Optimization techniques:
# - Tail-call elimination (not supported in Python by default).
# - Convert recursion into iteration for better performance.
# - Use memoization for repeated recursive calls (e.g., Fibonacci).


# ============================= practical lambda recursion use cases =========================
# Real-world scenarios where recursion (including lambda recursion) is useful:
# - Tree traversal (preorder, inorder, postorder)
# - Graph traversal (DFS, BFS)
# - Backtracking algorithms (e.g., N-Queens, Sudoku)
# - Dynamic programming (breaking problems into subproblems)

# Example: simple tree traversal using recursion
tree = {"value": 1, "children": [{"value": 2}, {"value": 3, "children": [{"value": 4}]}]}

def traverse(node):
    print(node["value"])
    for child in node.get("children", []):
        traverse(child)

traverse(tree)
# Output: 1 2 3 4
