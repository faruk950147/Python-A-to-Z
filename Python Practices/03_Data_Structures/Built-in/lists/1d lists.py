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
print(list1d[0])        # first element
print(list1d[-1])       # last element
print(list1d[1:3])      # slice
print(list1d[::-1])     # reverse using slicing


# ============================= 4. List Add Functions =============================
list1d.append(6)
list1d.extend([7, 8, 9])
list1d.insert(0, 0)


# ============================= 5. List Modify Functions =============================
list1d.sort()
list1d.reverse()
copy_list = list1d.copy()


# ============================= 6. List Delete Functions =============================
list1d.remove(6)
list1d.pop(6)
list1d.clear()


# ============================= 7. Looping List =============================
for i in range(len(list1d)):
    print(list1d[i])

for i in list1d:
    print(i)


# ============================= 8. List Comprehension =============================
squares = [x**2 for x in range(10)]           # [0,1,4,9,...,81]
even = [x for x in range(10) if x % 2 == 0]   # [0,2,4,6,8]
chars = [c.upper() for c in "python"]         # ['P','Y','T','H','O','N']


# ============================= 9. List Condition Functions =============================
list1d = [1, 2, 3, 4, 5]
print(any(x > 3 for x in list1d))   # True
print(all(x > 0 for x in list1d))   # True
print(max(list1d))                  # 5
print(min(list1d))                  # 1
print(sum(list1d))                  # 15


# =========================== 10. List Slicing ===========================
nums = [0,1,2,3,4,5,6,7,8,9]
print(nums[2:7])      # [2,3,4,5,6]
print(nums[:5])       # [0,1,2,3,4]
print(nums[5:])       # [5,6,7,8,9]
print(nums[::2])      # [0,2,4,6,8]
print(nums[::-1])     # reverse [9,8,...,0]
