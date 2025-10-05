# ============================= 1. What is List =============================
# → List is a collection of items in a specific order
# → List can contain duplicate items
# → List is mutable (change possible)
# → Python 3.7+ is ordered (insertion order preserved)
# → Item is indexed
# → Loop is iterable
# → Reference type, dynamic array based
# → All methods are available in list

# Common List Methods:
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


# ============================= 2. Basic 2D List =============================
list2d = [
    [1, 2],
    [3, 4]
]
print(f"list2d: {list2d}")                 # [[1, 2], [3, 4]] → 2D list
print(f"list2d[0]: {list2d[0]}")           # [1, 2] → row-0
print(f"list2d[1]: {list2d[1]}")           # [3, 4] → row-1
print(f"list2d[0][1]: {list2d[0][1]}")     # 2 → row-0 col-1
print(f"list2d[1][0]: {list2d[1][0]}")     # 3 → row-1 col-0

print("\n============================= 3. List Access Functions =============================")
list2d = [
    ['H', 'e', 'l', 'l', 'o'],
    ['W', 'o', 'r', 'l', 'd']
]
print(f"list2d: {list2d}")                 # [['H', 'e', 'l', 'l', 'o'], ['W', 'o', 'r', 'l', 'd']]
print(f"list2d[0]: {list2d[0]}")           # ['H', 'e', 'l', 'l', 'o'] → row-0
print(f"list2d[1]: {list2d[1]}")           # ['W', 'o', 'r', 'l', 'd'] → row-1
print(f"list2d[0][1]: {list2d[0][1]}")     # e → row-0 col-1
print(f"list2d[1][0]: {list2d[1][0]}")     # W → row-1 col-0
print(f"list2d[1][2]: {list2d[1][2]}")     # r → row-1 col-2


# ============================= 4. Row Slicing =============================
print("\n============================ Row Slicing =============================")
print(f"First two rows: {list2d[0:2]}")     # [['H', 'e', 'l', 'l', 'o'], ['W', 'o', 'r', 'l', 'd']]
print(f"Last row: {list2d[1:]}")            # [['W', 'o', 'r', 'l', 'd']]
print(f"All rows copy: {list2d[:]}")         # [['H', 'e', 'l', 'l', 'o'], ['W', 'o', 'r', 'l', 'd']]


# ============================= 5. Column Slicing =============================
print("\n============================ Column Slicing =============================")
print(f"First column: {[row[0] for row in list2d]}")     # ['H', 'W']
print(f"Second column: {[row[1] for row in list2d]}")    # ['e', 'o']
print(f"Last column: {[row[-1] for row in list2d]}")     # ['o', 'd']
print(f"Middle columns: {[row[1:3] for row in list2d]}")  # [['e', 'l'], ['o', 'r']]


# ============================= 6. Negative Indexing =============================
print("\n============================ Negative Indexing =============================")
print(f"Last row: {list2d[-1]}")                 # ['W', 'o', 'r', 'l', 'd']
print(f"Second last row: {list2d[-2]}")           # ['H', 'e', 'l', 'l', 'o']
print(f"Last column: {[row[-1] for row in list2d]}")         # ['o', 'd']
print(f"Second last column: {[row[-2] for row in list2d]}")  # ['l', 'r']


# ============================= 7. Diagonal Access (Square Matrix) =============================
print("\n============================ Diagonal Access =============================")
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(f"Main diagonal: {[matrix[i][i] for i in range(len(matrix))]}")        # [1, 5, 9]
print(f"Anti diagonal: {[matrix[i][len(matrix)-i-1] for i in range(len(matrix))]}")  # [3, 5, 7]


# ============================= 8. Reverse =============================
print("\n============================ Reverse =============================")
print(f"Row reverse: {list2d[::-1]}")                        # reverse rows
print(f"Column reverse: {[row[::-1] for row in list2d]}")    # reverse each row
print(f"Full reverse: {[row[::-1] for row in list2d[::-1]]}")  # reverse both


# ============================= 9. List Add Functions =============================
print("\n============================ List Add Functions =============================")
list2d = [
    [1, 2],
    [3, 4]
]
list2d[0].append(5)
print(f"list2d[0]: {list2d[0]}")   # [1, 2, 5]

list2d[1].insert(1, 6)
print(f"list2d[1]: {list2d[1]}")   # [3, 6, 4]

list2d[0].extend([7, 8])
print(f"list2d[0]: {list2d[0]}")   # [1, 2, 5, 7, 8]


# ============================= 10. List Modify Functions =============================
print("\n============================ List Modify Functions =============================")
list2d = [
    [1, 2],
    [3, 4]
]
list2d[0][1] = 20
print(f"list2d[0]: {list2d[0]}")   # [1, 20]

list2d[1] = [70, 80]
print(f"list2d[1]: {list2d[1]}")   # [70, 80]


# ============================= 11. List Delete Functions =============================
print("\n============================ List Delete Functions =============================")
list2d = [
    [1, 2],
    [3, 4]
]
list2d[0].remove(1)
print(f"list2d[0]: {list2d[0]}")   # [2]

list2d[1].pop()
print(f"list2d[1]: {list2d[1]}")   # [3]

list2d[0].clear()
print(f"list2d[0]: {list2d[0]}")   # []


# ============================= 12. Looping List =============================
print("\n============================ Looping List =============================")
list2d = [
    [10, 20],
    [30, 40]
]
for i in range(len(list2d)):
    for j in range(len(list2d[i])):
        print(list2d[i][j], end=" ")   # 10 20 30 40
print()

for row in list2d:
    for item in row:
        print(item, end=" ")           # 10 20 30 40
print()


# ============================= 13. List Comprehension =============================
print("\n============================ List Comprehension =============================")
list2d = [
    [1, 2],
    [3, 4]
]
flatten = [j for i in list2d for j in i]
print(f"flatten: {flatten}")   # [1, 2, 3, 4]


# ============================= 14. List Condition Functions =============================
print("\n============================ List Condition Functions =============================")
list2d = [
    [10, 20],
    [30, 40]
]
print(f"any(20 in row for row in list2d): {any(20 in row for row in list2d)}")   # True
print(f"all(all(k > 0 for k in row) for row in list2d): {all(all(k > 0 for k in row) for row in list2d)}") # True
print(f"20 in flatten: {20 in flatten}")      # True
print(f"100 not in flatten: {100 not in flatten}")  # True
