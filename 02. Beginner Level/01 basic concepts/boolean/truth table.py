# ========================== What Boolean Truth Table ===============================

# Boolean truth table
# A truth table is a mathematical table used in logic to compute the functional values of logical expressions on each combination of values taken by their logical variables.

# Basic Boolean Operations
# 1. NOT: Inverts the boolean value
# 2. AND: Returns True only if both operands are True
# 3. OR: Returns True if at least one operand is True

from itertools import product

# Generate all combinations of A and B (0=False, 1=True)
values = list(product([False, True], repeat=2))

# Print header
print("A\tB\tA AND B")

# Print truth table And
for A, B in values:
    print(f"{int(A)}\t{int(B)}\t{int(A and B)}")
    
# Now let's also show OR table
print("\nA\tB\tA OR B")
for A, B in values:
    print(f"{int(A)}\t{int(B)}\t{int(A or B)}")

# Now let's also show NOT table
print("\nA\tNOT A")
for A in [False, True]:
    print(f"{int(A)}\t{int(not A)}")

print("\nComplete Boolean Truth Tables:")