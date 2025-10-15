# common set creation
normal_set = {1, 2, 3}
print(normal_set)

# frozenset creation
frozen = frozenset([1, 2, 3, 3, 2])
print(frozen)

# frozen set is immutable
frozen.add(4) # AttributeError: 'frozenset' object has no attribute 'add'
print(frozen)
a = frozenset([1, 2, 3])
b = frozenset([3, 4, 5])

print(a | b)  # Union return all elements from both sets
print(a & b)  # Intersection return common elements
print(a - b)  # Difference return elements in a but not in b
print(a ^ b)  # Symmetric Difference return elements in either a or b but not both
a = frozenset([1, 2, 3])
b = frozenset([3, 4, 5])
print(a.isdisjoint(b))  # Disjoint return True if no common elements