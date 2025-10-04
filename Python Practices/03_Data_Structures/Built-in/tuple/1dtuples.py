# ============================= 1. What is Tuple =============================
# → Tuple is a collection of items in a specific order
# → every item is unique
# → Tuple is immutable (change not possible)
# → Python 3.7+ is ordered
# → item is indexed
# → loop is iterable
# → reference type, dynamic type, hash table based

# ============================= 2. Basic Tuple =============================
tuple1 = (1, 2, 3)
tuple2 = tuple([1, 2, 3])
tuple3 = tuple("abc")
tuple4 = tuple(range(1, 5))
tuple5 = tuple()

# ============================= 3. Tuple Access Functions =============================
print("\n============================ Tuple Access Functions =============================")
print(f"Initial tuple1: {tuple1}")
print(f"Initial tuple2: {tuple2}")
print(f"Initial tuple3: {tuple3}")
print(f"Initial tuple4: {tuple4}")
print(f"Initial tuple5: {tuple5}")
# Slice tuple1
print("\n============================ Tuple Slicing =============================")
print(f"Slice tuple1: {tuple1[1:3]}")
print(f"Reverse using slicing: {tuple1[::-1]}")
print(f"First 3 elements: {tuple1[:3]}")
print(f"Last 2 elements: {tuple1[3:]}")
print(f"Alternate elements: {tuple1[::2]}")
print(f"Reverse alternate elements: {tuple1[::-2]}")
print(f"Alternate elements from index 1: {tuple1[1::2]}")
print(f"Alternate elements from index -2: {tuple1[-2::-2]}")
print(f"Alternate elements from index -1: {tuple1[-1::-2]}")
print(f"Alternate elements from index -2: {tuple1[-2::-2]}")
print(f"Alternate elements from index -1: {tuple1[-1::-2]}")
# ============================= 4. Tuple Add Functions =============================
print("\n============================ Tuple Add Functions =============================")
tuple1d = (1, 2, 3)
tuple1d = tuple1d + (4, 5)
print(f"tuple1d (added): {tuple1d}")
tuple1d.append(6)
print(f"tuple1d (added): {tuple1d}")
tuple1d.extend([7, 8, 9])
print(f"tuple1d (added): {tuple1d}")
tuple1d.insert(0, 0)
print(f"tuple1d (added): {tuple1d}")

# ============================= 5. Tuple Modify Functions =============================
print("\n============================ Tuple Modify Functions =============================")
tuple1d = (1, 2, 3)
tuple1d.sort()        # sort tuple
tuple1d.reverse()     # reverse tuple
tuple1d.copy()        # shallow copy tuple

# ============================= 6. Tuple Delete Functions =============================
print("\n============================ Tuple Delete Functions =============================")
tuple1d = (1, 2, 3, 4, 5) 
tuple1d.pop(3) # Remove element at index 3
print(f"tuple1d (removed): {tuple1d}")
tuple1d.remove(2) # Remove element 2
tuple1d.clear() # Clear tuple
# del tuple1d # Delete tuple
# print("tuple1d (removed):", tuple1d)

# ============================= 7. Looping Tuple =============================
print("\n============================ Looping Tuple =============================")
tuple1d = (1, 2, 3, 4, 5)
for i in range(len(tuple1d)):
    print(tuple1d[i])

for i in tuple1d:
    print(i)

# ============================= 8. Tuple Comprehension =============================
print("\n============================ Tuple Comprehension =============================")
squares = (x**2 for x in range(10))           # (0,1,4,9,...,81)
even = (x for x in range(10) if x % 2 == 0)   # (0,2,4,6,8)
chars = (c.upper() for c in "python")         # ('P','Y','T','H','O','N')
print(f"squares: {squares}")
print(f"even: {even}")
print(f"chars: {chars}")








