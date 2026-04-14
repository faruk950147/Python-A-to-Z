def display_1(*args: int, callback: callable) -> int:
    if not args:
        return None

    result = args[0]
    for value in args[1:]:
        result = callback(result, value)
    return result

def add(a: int, b: int) -> int:
    return a + b

print(display_1(1, 2, 3, 4, 5, callback=add))
'''
Step 1: Argument Assign
args = (1, 2, 3, 4, 5)
callback = add
Step 2: Check Empty
if not args:
    return None

এখানে args empty না → তাই continue

Step 3: Initial Value
result = args[0] = 1
Step 4: Loop Execution
i = 1
result = add(1, 2) = 3
i = 2
result = add(3, 3) = 6
i = 3
result = add(6, 4) = 10
i = 4
result = add(10, 5) = 15

Final Return
return 15

Visualization (Simple)
1 + 2 = 3
3 + 3 = 6
6 + 4 = 10
10 + 5 = 15
Key Understanding

তোমার function আসলে:

custom reduce
প্রথম element → starting point
তারপর callback দিয়ে accumulate
'''