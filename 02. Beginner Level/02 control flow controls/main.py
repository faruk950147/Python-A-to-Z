# i = 0
# while (i := i + 1) <= 5:
#     print(f"i is {i}")

# Using walrus operator in a while loop
numbers = [1, 2, 3, 4, 5]
while (n := len(numbers)) > 0:
    print(f"List has {n} items")
    numbers.pop()

# Using walrus operator in list comprehension
# squares = [x**2 for x in range(10) if (y := x**2) > 20]
# print(squares)

