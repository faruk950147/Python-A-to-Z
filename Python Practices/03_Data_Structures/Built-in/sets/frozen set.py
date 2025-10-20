# ============================= what is Frozen Set =============================
# Frozen Set is an immutable set. It is created by the constructor "frozenset()".
# It is used when we need to make a set immutable.
a = frozenset([1, 2, 3])
print(a)    # frozenset({1, 2, 3})

# ============================= operations on frozen set =============================
a = frozenset([1, 2, 3])
b = frozenset([3, 4, 5])

print(a | b)  # Union return all elements from both sets
print(a & b)  # Intersection return common elements
print(a - b)  # Difference return elements in a but not in b
print(a ^ b)  # Symmetric Difference return elements in either a or b but not both
print(a.isdisjoint(b))  # Disjoint return True if no common elements
