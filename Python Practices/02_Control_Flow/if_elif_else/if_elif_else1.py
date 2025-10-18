a, b = list(map(int, input().split()))

# ======================== if ========================
# All conditions are checked separately
if a > b:
    print("a is greater than b")
if a < b:
    print("a is less than b")
if a == b:
    print("a is equal to b")
if a != b:
    print("a is not equal to b")

# ======================== elif rules ========================
# Only the condition true runs; others are conditionally not checked and skipped if true
# elif runs only if the previous conditions are false
if a > b:
    print("a is greater than b")
elif a < b:
    print("a is less than b")
elif a == b:
    print("a is equal to b")
else:
    print("a is not equal to b")

# ======================== Explanation ========================
# if → checks all conditions independently
# elif → checks one by one, stops after the first true condition
# else → runs only if none of the previous conditions are true
