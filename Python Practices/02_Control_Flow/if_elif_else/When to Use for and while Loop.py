# ============================ Loop Concept in Python ============================

# ============================ When to use for loop ============================
# Use for loop when:
# - We know the number of iterations (fixed)
# - We have a sequence of items (like list, tuple, string, range)
# - We want to iterate through each item in a sequence

# Syntax:
# for variable in sequence:
#     # statements

# Example 1: Using range (fixed iteration)
for i in range(5):
    print("Iteration:", i)

# Example 2: Using list
fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print("I like", fruit)


# ============================ When to use while loop ============================
# Use while loop when:
# - We don't know the number of iterations (unknown)
# - We have a condition that controls the loop
# - The loop should continue as long as the condition is True

# Syntax:
# while condition:
#     # statements

# Example 1: Condition-based
count = 0
while count < 5:
    print("Count is:", count)
    count += 1

# Example 2: User input based
password = ""
while password != "1234":
    password = input("Enter password: ")
print("Access granted!")


# ============================ Comparison (Summary) ============================
# for loop vs while loop

# | Feature              | for loop                            | while loop                         |
# |----------------------|--------------------------------------|------------------------------------|
# | Iteration count      | Known / fixed                        | Unknown / depends on condition     |
# | Based on             | Sequence or range                    | Condition                          |
# | Use Case             | Sequence traversal / fixed count     | Condition-based repetition         |
# | Example              | for i in range(10)                   | while i < 10                       |
# | Risk of infinite loop| Low                                  | High (if condition never becomes False) |

# ============================ Notes ============================
# Use for loop → when you have a known range or sequence
# Use while loop → when you have a condition-based repetition
# Be careful: while loop can cause infinite loop if condition never becomes False
