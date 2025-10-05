# ============================= 1. What is Tuple =============================
# → Tuple is a collection of items in a specific order
# → every item is unique
# → Tuple is immutable (change not possible)
# → Python 3.7+ is ordered
# → item is indexed
# → loop is iterable
# → reference type, dynamic type, hash table based

# ============================= 2. Basic Tuple =============================
tuple = (1) # Not tuple because it is not iterable and we can use () in int number a = (1) for example
tuple0 = (1,) # Tuple with single element it is iterable because used () and comma
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
tuple1 = ('H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd')

print(f"Slice tuple1 [1:3]: {tuple1[1:3]}")   
# ('e', 'l') → starts from index 1 ("e"), stops before index 3 ("l"), step = 1

print(f"Slice tuple1 [:3]: {tuple1[:3]}")     
# ('H', 'e', 'l') → start missing, defaults to 0, stops before index 3

print(f"Slice tuple1 [0:]: {tuple1[0:]}")     
# ('H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd') → full tuple

print(f"Slice tuple1 [:]: {tuple1[:]}")       
# same as full tuple (copy)

print(f"Slice tuple1 [::]: {tuple1[::]}")     
# same as full tuple (default step = 1)

print(f"Slice tuple1 [::2]: {tuple1[::2]}")   
# ('H', 'l', 'o', 'r', 'd') → every 2nd element

print(f"Slice tuple1 [::3]: {tuple1[::3]}")   
# ('H', 'l', ' ', 'r') → every 3rd element


# =============================== Negative Indexing ===============================
print("\n============================ Negative Indexing =============================")
print(f"Slice tuple1 [-1]: {tuple1[-1]}")   
# 'd' → last element

print(f"Slice tuple1 [-2:]: {tuple1[-2:]}")   
# ('l', 'd') → last 2 elements

print(f"Slice tuple1 [:-2]: {tuple1[:-2]}")   
# ('H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r') → all except last 2

print(f"Slice tuple1 [-2:-1]: {tuple1[-2:-1]}")   
# ('l',) → only the second last element

print(f"Slice tuple1 [-2:-3]: {tuple1[-2:-3]}")   
# () → empty tuple (because stop < start in forward direction)


# ============================= Tuple Reverse =============================
print("\n============================ Tuple Reverse =============================")
print(f"Slice tuple1 [::-1]: {tuple1[::-1]}")   
# ('d', 'l', 'r', 'o', 'W', ' ', 'o', 'l', 'l', 'e', 'H')

print(f"Slice tuple1 [::-2]: {tuple1[::-2]}")   
# ('d', 'r', 'W', 'l', 'H') → every 2nd element in reverse

print(f"Slice tuple1 [::-3]: {tuple1[::-3]}")   
# ('d', 'o', 'o', 'H') → every 3rd element in reverse

print(f"Slice tuple1 [::-4]: {tuple1[::-4]}")   
# ('d', 'W', 'l') → every 4th element in reverse

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








