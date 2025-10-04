# ============================= 1. What is List =============================
# → List is a collection of items in a specific order
# → Duplicate items allowed (not unique like set)
# → List is mutable (change possible)
# → Python 3.7+ maintains insertion order
# → Each item is indexed (0-based)
# → List is iterable (loop possible)
# → Reference type, dynamic type
# → Internally implemented as dynamic array (not hash table)
# → All methods are available in list
# → append() → add element at end
# → extend() → add multiple elements at end
# → insert() → add element at specific index
# → remove() → remove element
# → pop() → remove element at specific index
# → clear() → remove all elements
# → index() → index of element
# → count() → count of element
# → sort() → sort list
# → reverse() → reverse list
# → copy() → copy list
# → len(list) → length of list
# → max(list) → maximum element
# → min(list) → minimum element
# → sum(list) → sum of elements (if number)
# → sorted(list) → new sorted list
# → any(list) → True if any element is True
# → all(list) → True if all elements are True
# → enumerate(list) → index+value pair return
# → zip(list1, list2) → merge multiple lists
# → list(iterable) → iterable to list
# → all() → True if all elements are True
# → any() → True if any element is True

# → Some Functions not allowed in 3D list   
#
# ============================= 2. Basic List 3d =============================
# List creation
list3d = [
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
]

# ============================= 3. List Access Functions =============================
print(list3d)
print(list3d[0])
print(list3d[1])
print(list3d[0][1])
print(list3d[1][0])
print(list3d[0][1][0])
print(list3d[1][1][1])
# Output: 
# [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
# [[1, 2], [3, 4]]
# [[5, 6], [7, 8]]
# [3, 4]
# [5, 6]
# 3
# 8

# ============================= 4. List Add Functions =============================
list3d[0][0].append(11)
print(list3d[0][0])
# Output: [1, 2, 11]

list3d[1][0].insert(1, 60)
print(list3d[1][0])
# Output: [5, 60, 6]

list3d[0][1].extend([11, 12])
print(list3d[0][1])
# Output: [3, 4, 11, 12]

list3d[1][1].extend([70, 80])
print(list3d[1][1])
# Output: [7, 8, 70, 80]


# ============================= 5. List Modify Functions =============================
list3d[0][0][1] = 20
print(list3d[0][0])
# Output: [1, 20]

list3d[1][1] = [70, 80]
print(list3d[1])
# Output: [[5, 6], [70, 80]]

# using method
list3d[0][1].append(11)
print(list3d[0][1])
# Output: [3, 4, 11]

list3d[1][0].insert(1, 60)
print(list3d[1][0])
# Output: [5, 60, 6]


# ============================= 6. List Delete Functions =============================
list3d[0][1].remove(11)
print(list3d[0][1])
# Output: [3, 4]

list3d[1][0].pop(1)
print(list3d[1][0])
# Output: [5, 6]

list3d[0][1].clear()
print(list3d[0][1])
# Output: []

list3d[1][1].pop()
print(list3d[1][1])
# Output: [70]

list3d[0][0].remove(1)
print(list3d[0][0])
# Output: [20]

list3d[1][1].pop()
print(list3d[1][1])
# Output: [70]


# ============================= 7. Looping List =============================
for i in range(len(list3d)): # Range of list3d (2D list)
    for j in range(len(list3d[i])): # Range of list3d[i] (1D list)
        for k in range(len(list3d[i][j])): # Range of list3d[i][j] (1D list)
            print(list3d[i][j][k], end=" ")
# Output: 1 20 3 4 5 6 70 80 11

for i in list3d: # i is list3d[i] (1D list)
    for j in i: # j is list3d[i][j] (1D list)
        for k in j: # k is list3d[i][j][k] (1D list)
            print(k, end=" ")
# Output: 1 20 3 4 5 6 70 80 11

# ============================= 8. List Comprehension =============================
flatten = [list3d[i][j][k] for i in range(len(list3d)) for j in range(len(list3d[i])) for k in range(len(list3d[i][j]))]
print(flatten)
# Output: [1, 20, 3, 4, 5, 6, 70, 80, 11]

flatten = [k for i in list3d for j in i for k in j]
print(flatten)
# Output: [1, 20, 3, 4, 5, 6, 70, 80, 11]

# ============================= 9. List condition Functions =============================
print(any(k == 70 for i in range(len(list3d)) for j in range(len(list3d[i])) for k in range(len(list3d[i][j]))))   # True
print(all(k > 0 for i in range(len(list3d)) for j in range(len(list3d[i])) for k in range(len(list3d[i][j]))))     # True
print(20 in flatten)   # True
print(100 not in flatten) # True

# ============================= 10. List Slicing =============================
# [start:stop:step]
