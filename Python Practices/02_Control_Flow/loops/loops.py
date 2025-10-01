
# 1. for loop

# Used to iterate over sequences (lists, strings, ranges).

# Example: print numbers 1 to 5
for i in range(1, 6):
    print(i)


# Output:

# 1
# 2
# 3
# 4
# 5


# Iterating over a list:

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)


# Output:

# apple
# banana
# cherry

# Example: print fruits
fruits = ["apple", "banana", "cherry"]
for fruit in range(len(fruits)):
    print(fruits[fruit])


# Output:

# apple
# banana
# cherry

# 2. while loop

# Runs as long as a condition is True.

i = 1
while i <= 5:
    print(i)
    i += 1


# Output:

# 1
# 2
# 3
# 4
# 5

# 3. Loop control statements

# break → stop the loop immediately

for i in range(1, 6):
    if i == 3:
        break
    print(i)


# Output:

# 1
# 2


# continue → skip the current iteration

for i in range(1, 6):
    if i == 3:
        continue
    print(i)


# Output:

# 1
# 2
# 4
# 5

