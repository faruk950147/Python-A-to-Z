# Iteration by iteration:

# First iteration:

# Current element in iteration: 'a'

# Assign to lst[-1]: lst[-1] = 'a'

# Now lst = ['a', 'b', 'c', 'a']

# print(lst[-1]) → prints a

# Second iteration:

# Current element in iteration: 'b'

# Assign to lst[-1]: lst[-1] = 'b'

# Now lst = ['a', 'b', 'c', 'b']

# print(lst[-1]) → prints b

# Third iteration:

# Current element in iteration: 'c'

# Assign to lst[-1]: lst[-1] = 'c'

# Now lst = ['a', 'b', 'c', 'c']

# print(lst[-1]) → prints c

# Fourth iteration:

# Current element in iteration: 'c' (note: last element of the list was updated in the previous step, so the last element is 'c' now)

# Assign to lst[-1]: lst[-1] = 'c'

# lst stays the same: ['a', 'b', 'c', 'c']

# print(lst[-1]) → prints c

lst = ['a', 'b', 'c', 'd']
for lst[-1] in lst:
    print(lst[-1], end=" ")