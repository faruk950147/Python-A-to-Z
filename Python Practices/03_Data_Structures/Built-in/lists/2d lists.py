# ============================= 1. What is List =============================
# → List is a collection of items in a specific order
# → every item is unique
# → List is mutable (change possible)
# → Python 3.7+ is ordered
# → item is indexed
# → loop is iterable
# → reference type, dynamic type, hash table based
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

# ============================= 2. Basic List 2d =============================
# List creation
list2d = [
    [1, 2],
    [3, 4]
]

print("============================= 2. List Access Functions =============================")
# ============================= 3. List Access Functions =============================
list2d = [
    [1, 2],
    [3, 4]
]
print(f"list2d: {list2d}")
print(f"list2d[0]: {list2d[0]}")
print(f"list2d[1]: {list2d[1]}")
print(f"list2d[0][1]: {list2d[0][1]}")
print(f"list2d[1][0]: {list2d[1][0]}")
# Slicing
print("============================= 3. List Slicing Functions =============================")
print(f"list2d[0][1:]: {list2d[0][1:]}")
print(f"list2d[1][1:]: {list2d[1][1:]}")

print("============================= 4. List Add Functions =============================")
# ============================= 4. List Add Functions =============================
list2d = [
    [1, 2],
    [3, 4]
]
list2d[0].append(5)
print(f"list2d[0]: {list2d[0]}")
# Output: [1, 2, 5]

list2d[1].insert(1, 6)
print(f"list2d[1]: {list2d[1]}")
# Output: [3, 6, 4]

list2d[0].extend([7, 8])
print(f"list2d[0]: {list2d[0]}")
# Output: [1, 2, 5, 7, 8]

list2d[1].extend([9, 10])
print(f"list2d[1]: {list2d[1]}")
# Output: [3, 6, 4, 9, 10]

print("============================= 5. List Modify Functions =============================")
# ============================= 5. List Modify Functions =============================
list2d = [
    [1, 2],
    [3, 4]
]
list2d[0][1] = 20
print(f"list2d[0]: {list2d[0]}")
# Output: [1, 20]

list2d[1] = [70, 80]
print(f"list2d[1]: {list2d[1]}")
# Output: [70, 80]

print("============================= 6. List Delete Functions =============================")
# ============================= 6. List Delete Functions =============================
list2d = [
    [1, 2],
    [3, 4]
]
list2d[0].remove(1)
print(f"list2d[0]: {list2d[0]}")
# Output: [20]

list2d[1].pop()
print(f"list2d[1]: {list2d[1]}")
# Output: [70]

list2d[0].clear()
print(f"list2d[0]: {list2d[0]}")
# Output: []

list2d[1].pop()
print(f"list2d[1]: {list2d[1]}")
# Output: [70]

print("============================= 7. Looping List =============================")
# ============================= 7. Looping List =============================
list2d = [
    [1, 2],
    [3, 4]
]
for i in range(len(list2d)):
    for j in range(len(list2d[i])):
        print(list2d[i][j], end=" ")
# Output: 20 70

for i in list2d:
    for j in i:
        print(j, end=" ")
# Output: 20 70

print("============================= 8. List Comprehension =============================")
# ============================= 8. List Comprehension =============================
list2d = [
    [1, 2],
    [3, 4]
]
flatten = [list2d[i][j] for i in range(len(list2d)) for j in range(len(list2d[i]))]
print(f"flatten: {flatten}")
# Output: [20, 70]

flatten = [k for i in list2d for j in i for k in j]
print(f"flatten: {flatten}")
# Output: [20, 70]

print("============================= 9. List condition Functions =============================")
# ============================= 9. List condition Functions =============================
list2d = [
    [1, 2],
    [3, 4]
]
print(f"any(k == 70 for i in range(len(list2d)) for j in range(len(list2d[i])) for k in range(len(list2d[i][j]))): {any(k == 70 for i in range(len(list2d)) for j in range(len(list2d[i])) for k in range(len(list2d[i][j])))}")   # True
print(f"all(k > 0 for i in range(len(list2d)) for j in range(len(list2d[i])) for k in range(len(list2d[i][j]))): {all(k > 0 for i in range(len(list2d)) for j in range(len(list2d[i])) for k in range(len(list2d[i][j])))}")     # True
print(f"20 in flatten: {20 in flatten}")   # True
print(f"100 not in flatten: {100 not in flatten}") # True
