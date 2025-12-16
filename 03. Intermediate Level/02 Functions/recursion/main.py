import sys

max_recursion_depth = sys.getrecursionlimit() - 1

def demo(n):
    if n == 0:
        return
    print("demo", n)
    demo(n + 1)

demo(max_recursion_depth)
# limit 1997