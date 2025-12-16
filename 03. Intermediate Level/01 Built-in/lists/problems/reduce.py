from functools import reduce
# reduce() takes two parameters:
# 1. function
# 2. iterable
# ============================= what is reduce? =============================
# reduce() is a function that takes a function and an iterable as arguments.
# It applies the function to the first two items in the iterable and then to the result and the next item, and so on.
# It returns a single value.
# ============================= example =============================
def add(x, y):
    return x + y

print(reduce(add, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# ============================= working flow of reduce =============================
# step 1: add(1, 2) → 3
# step 2: add(3, 3) → 6
# step 3: add(6, 4) → 10
# step 4: add(10, 5) → 15
# step 5: add(15, 6) → 21
# step 6: add(21, 7) → 28
# step 7: add(28, 8) → 36
# step 8: add(36, 9) → 45
# step 9: add(45, 10) → 55

# 1 + 2 = 3
# 3 + 3 = 6
# 6 + 4 = 10
# 10 + 5 = 15
# 15 + 6 = 21
# 21 + 7 = 28
# 28 + 8 = 36
# 36 + 9 = 45
# 45 + 10 = 55

def max(x, y):
    return x if x > y else y

print(reduce(max, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# ============================= working flow of reduce =============================
# step 1: max(1, 2) → 2
# step 2: max(2, 3) → 3
# step 3: max(3, 4) → 4
# step 4: max(4, 5) → 5
# step 5: max(5, 6) → 6
# step 6: max(6, 7) → 7
# step 7: max(7, 8) → 8
# step 8: max(8, 9) → 9
# step 9: max(9, 10) → 10
