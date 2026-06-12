'''
a = {1, 2, 3}

# common elements a and b are {1, 2}
b = {1, 2}  # it is a subset of a
print(b.issubset(a))  # True

# how many elements in world (universal set)
u = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# common elements and unique elements
a = {1, 2, 3}
b = {1, 3, 4, 5}
union = {1, 2, 3, 4, 5}
print(a.union(b))


# just common elements
a = {1, 2, 3}
b = {1, 3, 4, 5}
intersection = {1, 3}
print(intersection)

'''