# ============================= 1. What is List =============================
# → List is a collection of items in a specific order
# → Duplicate items allowed (not unique)
# → List is mutable (change possible)
# → Python 3.7+ maintains insertion order
# → Each item is indexed (0-based)
# → List is iterable (loop possible)
# → Reference type, dynamic type
# → Internally implemented as dynamic array

# → Common List Methods
# append()   → add element at end
# extend()   → add multiple elements at end
# insert()   → add element at specific index
# remove()   → remove element
# pop()      → remove element at specific index
# clear()    → remove all elements
# index()    → index of element
# count()    → count of element
# sort()     → sort list
# reverse()  → reverse list
# copy()     → shallow copy
# len(list)  → length of list
# max(list)  → maximum element
# min(list)  → minimum element
# sum(list)  → sum of elements (if numbers)
# sorted(list) → returns new sorted list
# any(list)  → True if any element is True
# all(list)  → True if all elements are True
# enumerate(list) → index+value pairs
# zip(list1, list2) → merge multiple lists
# list(iterable)   → iterable to list


# ============================= 2. Basic List 1d =============================
list1d = [1, 2, 3, 4, 5]
list1d = list(range(1, 6))
list1d = list("12345")   # ['1','2','3','4','5']


# ============================= 3. List Access Functions =============================
print("\n============================ List Access Functions =============================")
print(f"First element: {list1d[0]}")        # first element
print(f"Last element: {list1d[-1]}")       # last element

print("\n============================ List Slicing =============================")
list1 = ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']

print(f"Slice list1 [1:3]: {list1[1:3]}")   
# ['e', 'l'] → starts from index 1, stops before index 3

print(f"Slice list1 [:3]: {list1[:3]}")     
# ['H', 'e', 'l'] → start missing (default 0), stops before index 3

print(f"Slice list1 [0:]: {list1[0:]}")     
# ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd'] → full list

print(f"Slice list1 [:]: {list1[:]}")       
# full list (copy)

print(f"Slice list1 [::]: {list1[::]}")     
# full list (step default = 1)

print(f"Slice list1 [::2]: {list1[::2]}")   
# ['H', 'l', 'o', 'r', 'd'] → every 2nd element

print(f"Slice list1 [::3]: {list1[::3]}")   
# ['H', 'l', ' ', 'r'] → every 3rd element


# =============================== Negative Indexing ===============================
print("\n============================ Negative Indexing =============================")
print(f"Slice list1 [-1]: {list1[-1]}")   
# 'd' → last element

print(f"Slice list1 [-2:]: {list1[-2:]}")   
# ['l', 'd'] → last 2 elements

print(f"Slice list1 [:-2]: {list1[:-2]}")   
# ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r'] → all except last 2

print(f"Slice list1 [-2:-1]: {list1[-2:-1]}")   
# ['l'] → only the second last element

print(f"Slice list1 [-2:-3]: {list1[-2:-3]}")   
# [] → empty list (because stop < start in forward slicing)


# ============================= List Reverse =============================
print("\n============================ List Reverse =============================")
print(f"Slice list1 [::-1]: {list1[::-1]}")   
# ['d', 'l', 'r', 'o', 'W', ' ', 'o', 'l', 'l', 'e', 'H']

print(f"Slice list1 [::-2]: {list1[::-2]}")   
# ['d', 'r', 'W', 'l', 'H'] → every 2nd element in reverse

print(f"Slice list1 [::-3]: {list1[::-3]}")   
# ['d', 'o', 'o', 'H'] → every 3rd element in reverse

print(f"Slice list1 [::-4]: {list1[::-4]}")   
# ['d', 'W', 'l'] → every 4th element in reverse



# ============================= 4. List Add Functions =============================
print("\n============================ List Add Functions =============================")
list1 = [1, 2, 3]
# append()   → add element at end
# extend()   → add multiple elements at end
# insert()   → add element at specific index
list1.append(6)        # add element at end
list1.extend([7, 8, 9]) # add multiple elements at end
list1.insert(0, 0)     # add element at specific index

print(f"list1: {list1}")


# ============================= 5. List Modify Functions =============================
print("\n============================ List Modify Functions =============================")
list1d = [1, 2, 3]
# sort()     → sort list
# reverse()  → reverse list
# copy()     → shallow copy
list1d.sort()        # sort list
list1d.reverse()     # reverse list
copy_list = list1d.copy() # shallow copy

print(f"list1d: {list1d}")
print(f"copy_list: {copy_list}")


# ============================= 6. List Delete Functions =============================
print("\n============================ List Delete Functions =============================")
list1d = [1, 2, 3, 4, 5, 6]
list1d.remove(2)
list1d.pop(3)
list1d.clear()


# ============================= 7. Looping List =============================
print("\n============================ Looping List =============================")
list1d = [1, 2, 3, 4, 5]
for i in range(len(list1d)):
    print(list1d[i])

for i in list1d:
    print(i)


# ============================= 8. List Comprehension =============================
print("\n============================ List Comprehension =============================")
squares = [x**2 for x in range(10)]           # [0,1,4,9,...,81]
even = [x for x in range(10) if x % 2 == 0]   # [0,2,4,6,8]
chars = [c.upper() for c in "python"]         # ['P','Y','T','H','O','N']

print(f"squares: {squares}")
print(f"even: {even}")
print(f"chars: {chars}")


# ============================= 9. List Condition Functions =============================
print("\n============================ List Condition Functions =============================")
list1d = [1, 2, 3, 4, 5]
print(f"any(x > 3 for x in list1d): {any(x > 3 for x in list1d)}")   # True
print(f"all(x > 0 for x in list1d): {all(x > 0 for x in list1d)}")   # True
print(f"max(list1d): {max(list1d)}")                  # 5
print(f"min(list1d): {min(list1d)}")                  # 1
print(f"sum(list1d): {sum(list1d)}")                  # 15