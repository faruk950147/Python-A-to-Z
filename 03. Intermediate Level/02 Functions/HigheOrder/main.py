
from functools import reduce

# map(), filter(), reduce(), sorted(), any(), all()
def square(x):
    return x * x

print(f"list(map(square, range(1, 6))): {list(map(square, range(1, 6)))}")

print(f"list(filter(lambda x: x % 2 == 0, range(1, 6))): {list(filter(lambda x: x % 2 == 0, range(1, 6)))}")

print(f"reduce(lambda x, y: x + y, range(1, 6)): {reduce(lambda x, y: x + y, range(1, 6))}")

print(f"sorted([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]): {sorted([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])}")

print(f"any([False, False, True]): {any([False, False, True])}")

print(f"all([True, True, True]): {all([True, True, True])}")

