# ============================= Symmetric Difference =============================
# Symmetric Difference is a set of all elements that are in set A or set B but not in both.
# Symmetric Difference is a uncommon element between set A and set B.
# Symmetric Difference is denoted by the symbol "Δ".
a = {1, 2, 3}
b = {3, 4, 5}

print(a.symmetric_difference(b)) # {1, 2, 4, 5}
print(a ^ b) # {1, 2, 4, 5}
