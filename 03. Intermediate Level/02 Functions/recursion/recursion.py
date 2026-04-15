# ============================= What is Recursion =============================
# Recursion is a technique where a function calls itself.
# It breaks a big problem into smaller subproblems until a base condition is met.

import sys

# ============================= Basic Recursion ===============================
# Simple examples of recursive functions

max_recursion_depth = sys.getrecursionlimit() - 1
print("Max recursion depth:", max_recursion_depth)

def demo(n):
    if n == 0:
        return
    print("demo", n)
    demo(n - 1)

demo(5)

# Countdown example
'''
def count_down(n):
    if n == 0:          # Base case
        return n
    print(n)
    count_down(n - 1)   # Recursive case

print("Countdown:")
count_down(5)
print("===============")


# ============================= Factorial Using Recursion =====================

def factorial(n):
    if n == 1:          # Base case
        return 1
    return n * factorial(n - 1)  # Recursive case

print("Factorial of 5:", factorial(5))
print("===============")


# ============================= Fibonacci Using Recursion =====================

def fibonacci(n):
    if n <= 1:          # Base case
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print("First 10 Fibonacci numbers:")
for i in range(10):
    print(fibonacci(i), end=" ")
print("\n===============")


# ============================= Tail Recursion ================================
# Tail recursion is when the recursive call is the last thing the function does.
# It leaves no pending operations.

def tail_factorial(n, acc=1):
    if n == 1:
        return acc
    return tail_factorial(n - 1, n * acc)

print("Tail Recursion Factorial of 5:", tail_factorial(5))
print("===============")

# ============================= Tail vs Normal Recursion ======================
# | Aspect           | Normal Recursion     | Tail Recursion         |
# |------------------|----------------------|------------------------|
# | Work remaining   | After the call       | None after the call    |
# | Memory usage     | Higher (deep stack)  | Lower (stack reuse)    |
# | Performance      | Slower               | Faster (in other langs)|


# ============================= Practical Use Cases ==========================
# - Tree Traversal
# - Graph Traversal
# - Backtracking


# ============================= 1. Tree Traversal Example =====================

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def inorder(root):
    if root:
        inorder(root.left)
        print(root.value, end=" ")
        inorder(root.right)

# Build a simple tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Inorder Traversal of Tree:")
inorder(root)
print("\n===============")


# ============================= 2. Graph Traversal (DFS) =====================

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

visited = set()

def dfs(node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbor in graph[node]:
            dfs(neighbor)

print("Graph DFS Traversal:")
dfs('A')
print("\n===============")


# ============================= 3. Backtracking Example ======================
# Example: Print all permutations of [1, 2, 3]

def backtrack(path, choices):
    if not choices:
        print(path)
        return
    for i in range(len(choices)):
        backtrack(path + [choices[i]], choices[:i] + choices[i+1:])

print("All permutations of [1, 2, 3]:")
backtrack([], [1, 2, 3])
print("===============")


# ============================= Summary ======================================
# Recursion means a function calling itself.
# Every recursive function must have a base case to stop it.
# Tail recursion is memory efficient, but Python does NOT support TCO (Tail Call Optimization).
# Common uses: Tree/Graph traversal, Backtracking, Divide & Conquer algorithms.
'''
