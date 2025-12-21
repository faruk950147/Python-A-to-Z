
# 1. for loop
# Loop Rules (Very Important)
#
# Rule 1
# A loop starts with an initial value.
#
# Rule 2
# The condition is checked before every iteration.
#
# Rule 3
# If the condition is true, the loop body executes.
#
# Rule 4
# After executing the loop body, the update (increment/decrement) happens.
#
# Rule 5
# If the condition becomes false, the loop stops.
#
# Rule 6 (Interview Line ⭐)
# A loop continues to run as long as its condition remains true

"""
             ┌───────────────┐
             │   Start        │
             └───────┬───────┘
                     │
              ┌──────▼────────┐
              │ Initialize i=1│
              └───────┬───────┘
                      │
              ┌───────▼────────┐
              │ i in range ?   │
              └───┬──────┬─────┘
                  │Yes   │No
                  │      │
          ┌───────▼───┐  │
          │ print(i)  │  │
          └───────┬───┘  │
                  │      │
          ┌───────▼─────┐│
          │ i = i + 1   ││
          └───────┬─────┘│
                  │       │
                  └───────┘


"""

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

"""
             ┌───────────────┐
             │   Start        │
             └───────┬───────┘
                     │
              ┌──────▼────────┐
              │  i = 1        │
              └───────┬───────┘
                      │
              ┌───────▼────────┐
              │ i <= 5 ?       │
              └───┬─────┬──────┘
                  │Yes  │No
                  │     │
          ┌───────▼─┐   │
          │ print(i)│   │
          └───────┬─┘   │
                  │     │
          ┌───────▼─────┐
          │ i = i + 1   │
          └───────┬─────┘
                  │
                  └───> (back to check i <= 5)


"""
# ============================= positive looping =============================

# ===================== while loop =====================
i = 1
while i <= 5:
    print('Hello World')
    i += 1

# Output:

# Hello World
# Hello World
# Hello World
# Hello World
# Hello World

i = 1
while i <= 5:
    print(i)
    i += 1

while True: # infinite loop
    print('Hello World')
    


# ===================== for loop =====================
for _ in range(1, 6):
    print('Hello World')
    
for i in range(1, 6):
    print(i)    
    
# ===================== negative looping =====================

# ===================== while loop =====================
i = 5
while i >= 1:
    print(i)
    i -= 1
    
# Output:

# 5
# 4
# 3
# 2
# 1

# ===================== for loop =====================
for i in range(5, 0, -1):
    print(i)
    
# Output:

# 5
# 4
# 3
# 2
# 1

# ============================= break and continue while loop =============================

# break
i = 1
while i <= 5:
    if i == 3:
        break
    print(i)
    i += 1

# Output:

# 1
# 2

# continue
i = 1
while i <= 5:
    if i == 3:
        continue
    print(i)
    i += 1

# Output:

# 1
# 2
# 4
# 5

i = 1
while True:
    if i == 3:
        break
    print(i)
    i += 1

# ============================= break and continue for loop =============================

# break
for i in range(1, 6):
    if i == 3:
        break
    print(i)

# Output:

# 1
# 2

# continue
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

# Output:

# 1
# 2
# 4
# 5