""" nested in python
Nested Loop Rules (Very Important)
    Rule 1
        When the outer loop runs once, the inner loop runs completely.

    Rule 2

        The outer loop does not move to the next value until the inner loop finishes.

    Rule 3

        For every new value of the outer loop, the inner loop starts again from the beginning.

    Rule 4

        The outer loop controls how many times the process repeats.
        The inner loop controls what happens in each repetition.

    Rule 5 (Interview Line)

        For each iteration of the outer loop, the inner loop executes fully.

        Simple Formula
        Total operations = outer loop × inner loop """

for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)

for i in range(3):
    for j in range(3):
        print("*", end=" ")
    print()

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for item in row:
        print(item, end=" ")
    print()
