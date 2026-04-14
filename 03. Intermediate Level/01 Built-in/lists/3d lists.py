# ============================= 1. What is List =============================
# → List is a collection of items in a specific order
# → Duplicate items allowed
# → List is mutable (change possible)
# → Python 3.7+ maintains insertion order
# → Each item is indexed (0-based)
# → List is iterable (loop possible)
# → Reference type, dynamic array based
# → Implemented using dynamic array (NOT hash table)

# Common List Methods:
# append()   → add element at end
# extend()   → add multiple elements at end
# insert()   → add element at specific index
# remove()   → remove element by value
# pop()      → remove element by index (default last)
# clear()    → remove all elements
# index()    → find index of element
# count()    → count occurrences
# sort()     → sort list (in-place)
# reverse()  → reverse list (in-place)
# copy()     → shallow copy
# len(list)  → length of list
# max(list)  → maximum value
# min(list)  → minimum value
# sum(list)  → sum of numbers
# sorted(list) → new sorted list
# any(list)  → True if any element is True
# all(list)  → True if all elements is True
# enumerate(list) → index + value pairs
# zip(list1, list2) → merge lists
# list(iterable) → convert iterable to list


# ============================= 2. Basic 3D List =============================

list3d = [
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
]

print(list3d)


# ============================= 3. List Access =============================

list3d = [
    [
        ['H', 'e', 'l', 'l', 'o'],
        ['W', 'o', 'r', 'l', 'd']
    ],
    [
        ['H', 'e', 'l', 'l', 'o'],
        ['W', 'o', 'r', 'l', 'd']
    ]
]

print(list3d[0])
print(list3d[1])
print(list3d[0][1])
print(list3d[1][0])
print(list3d[1][2])
print(list3d[0][0][0])
print(list3d[0][1][0])
print(list3d[1][0][0])
print(list3d[1][1][0])



# ============================= 4. Row Slicing =============================

print(list3d[0:2])
print(list3d[1:])
print(list3d[:])


# ============================= 5. Column Slicing =============================

print([row[0] for row in list3d])
print([row[1] for row in list3d])
print([row[-1] for row in list3d])
print([row[1:3] for row in list3d])


# ============================= 6. Negative Indexing =============================

print(list3d[-1])
print(list3d[-2])
print([row[-1] for row in list3d])
print([row[-2] for row in list3d])


# ============================= 7. Diagonal Access =============================

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print([matrix[i][i] for i in range(len(matrix))])
print([matrix[i][len(matrix)-i-1] for i in range(len(matrix))])


# ============================= 8. Reverse =============================

print(list3d[::-1])
print([row[::-1] for row in list3d])
print([row[::-1] for row in list3d[::-1]])


# ============================= 9. Add Functions =============================

list3d[0][0].append(11)
list3d[1][0].insert(1, 60)
list3d[0][1].extend([11, 12])
list3d[1][1].extend([70, 80])

print(list3d)


# ============================= 10. Modify Functions =============================

list3d[0][0][1] = 20
list3d[1][1] = [70, 80]

list3d[0][1].append(11)
list3d[1][0].insert(1, 60)

print(list3d)


# ============================= 11. Delete Functions =============================

list3d[0][1].remove(11)
list3d[1][0].pop(1)
list3d[0][1].clear()
list3d[1][1].pop()
list3d[0][0].remove(1)
list3d[1][1].pop()

print(list3d)


# ============================= 12. Looping 3D List =============================

for i in list3d:
    for j in i:
        for k in j:
            print(k, end=" ")
print()


# ============================= 13. List Comprehension =============================

flatten = [k for i in list3d for j in i for k in j]
print(flatten)


# ============================= 14. Condition Functions =============================

print(any(k == 70 for i in list3d for j in i for k in j))
print(all(k > 0 for i in list3d for j in i for k in j))
print(20 in flatten)
print(100 not in flatten)