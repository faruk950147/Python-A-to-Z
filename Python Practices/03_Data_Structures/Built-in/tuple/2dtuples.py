# ============================= 1. What is Tuple =============================
# → Tuple is a collection of items in a specific order
# → every item is unique
# → Tuple is immutable (change not possible)
# → Python 3.7+ is ordered
# → item is indexed
# → loop is iterable
# → reference type, dynamic type, hash table based  

# ============================= 2. Basic 2D Tuple =============================
tuple1 = ((1, 2, 3), (4, 5, 6))

print("\n============================ Tuple Access Functions =============================")
# ============================= 3. Tuple Access Functions =============================
print(f"tuple1 (accessed): {tuple1}")
print(f"tuple1 (accessed): {tuple1[0]}")
print(f"tuple1 (accessed): {tuple1[1]}")
print(f"tuple1 (accessed): {tuple1[0][0]}")
print(f"tuple1 (accessed): {tuple1[0][1]}")
print(f"tuple1 (accessed): {tuple1[0][2]}")
print(f"tuple1 (accessed): {tuple1[1][0]}")
print(f"tuple1 (accessed): {tuple1[1][1]}")
print(f"tuple1 (accessed): {tuple1[1][2]}")
# Slice
print("\n============================ Tuple Slicing =============================")
print(f"tuple1 (accessed): {tuple1[0:2]}")
print(f"tuple1 (accessed): {tuple1[0:2][0]}")
print(f"tuple1 (accessed): {tuple1[0:2][1]}")
print(f"tuple1 (accessed): {tuple1[0:2][0][0]}")
print(f"tuple1 (accessed): {tuple1[0:2][0][1]}")
print(f"tuple1 (accessed): {tuple1[0:2][0][2]}")
print(f"tuple1 (accessed): {tuple1[0:2][1][0]}")
print(f"tuple1 (accessed): {tuple1[0:2][1][1]}")
print(f"tuple1 (accessed): {tuple1[0:2][1][2]}")

print("\n================================== Tuple Add Functions===================================")
# ============================= Tuple Add Functions =============================
tuple1d = ((1, 2, 3), (4, 5, 6))
tuple1d = tuple1d + ((7, 8, 9), (10, 11, 12))
print(f"tuple1d (added): {tuple1d}")
tuple1d.append((13, 14, 15))
print(f"tuple1d (added): {tuple1d}")
tuple1d.extend([(16, 17, 18), (19, 20, 21)])
print(f"tuple1d (added): {tuple1d}")
tuple1d.insert(0, (0, 0, 0))
print(f"tuple1d (added): {tuple1d}")

print("\n================================== Tuple Modify Functions===================================")
# ============================= Tuple Modify Functions =============================
tuple1d = ((1, 2, 3), (4, 5, 6))
tuple1d.sort()        # sort tuple
tuple1d.reverse()     # reverse tuple
tuple1d.copy()        # shallow copy tuple

print("\n================================== Tuple Delete Functions===================================")
# ============================= Tuple Delete Functions =============================
tuple1d = ((1, 2, 3), (4, 5, 6))
tuple1d.pop(3) # Remove element at index 3
tuple1d.remove(2) # Remove element 2
tuple1d.clear() # Clear tuple
# del tuple1d # Delete tuple
# print("tuple1d (removed):", tuple1d)

print("\n================================== Tuple Loop Functions===================================")
# ============================= Tuple Loop Functions =============================
tuple1d = ((1, 2, 3), (4, 5, 6))
for i in range(len(tuple1d)):
    print(tuple1d[i])

for i in tuple1d:
    print(i)

print("\n================================== Tuple Comprehension Functions===================================")
# ============================= Tuple Comprehension Functions =============================
tuple1d = ((1, 2, 3), (4, 5, 6))
squares = (x**2 for x in range(10))           # (0,1,4,9,...,81)
even = (x for x in range(10) if x % 2 == 0)   # (0,2,4,6,8)
chars = (c.upper() for c in "python")         # ('P','Y','T','H','O','N')
print(f"squares: {squares}")
print(f"even: {even}")
print(f"chars: {chars}")
