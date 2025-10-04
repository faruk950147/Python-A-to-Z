# ============================= 1. What is Set =============================
# → Set is a collection of items in a specific order
# → every item is unique
# → Set is mutable (change possible)
# → Python 3.7+ is ordered
# → item is indexed
# → loop is iterable
# → reference type, dynamic type, hash table based

print("============================ 2. Basic Set =============================")
# ============================= 2. Basic Set =============================
set1 = {1, 2, 3}
set2 = set([1, 2, 3])
set3 = set("abc")
set4 = set(range(1, 5))
set5 = set()

print("\n============================ 3. Set Access Functions =============================")
# ============================= 3. Set Access Functions =============================

print("Initial set1:", set1)
print("Initial set2:", set2)
print("Initial set3:", set3)
print("Initial set4:", set4)
print("Initial set5:", set5)

print("\n============================ 4. Set Add Functions =============================")  
# ============================= 4. Set Add Functions =============================
set1.add(4)                    # Single value add
set2.update([5, 6])            # Multiple values add
set3.update("def")             # String values add
set4.update(range(5, 8))       # Range values add
set5.add(1)

print("\nAfter Add:")
print("set1:", set1)
print("set2:", set2)
print("set3:", set3)
print("set4:", set4)
print("set5:", set5)

print("\n============================ 5. Set Modify Functions =============================")
# ============================= 5. Set Modify Functions =============================
set1.remove(4)         # if element not found error 
set2.discard(5)        # if element not found no error 
set3.pop()             # random element remove 
set4.clear()           # clear all elements
set5.discard(1)

print("\nAfter Modify:")
print("set1:", set1)
print("set2:", set2)
print("set3:", set3)
print("set4:", set4)
print("set5:", set5)

print("\n============================ 6. Set Delete Functions =============================")
# ============================= 6. Set Delete Functions =============================
# pop()     only works when set is not empty
if set1:
    set1.pop()
if set2:
    set2.pop()
if set3:
    set3.pop()
if set4:   # set4 is already empty
    set4.pop()
if set5:   # set5 discard 1
    set5.pop()

print("\nAfter Delete:")
print("set1:", set1)
print("set2:", set2)
print("set3:", set3)
print("set4:", set4)
print("set5:", set5)

print("\n============================ 7. Looping Set =============================")
# ============================= 7. Looping Set =============================
print("\nLooping set1:")
for item in set1:
    print(item)

print("\n============================ 8. Set Comprehension =============================")
# ============================= 8. Set Comprehension =============================
set6 = {x for x in range(1, 5)}
print("\nset6 (comprehension):", set6)

print("\n============================ 9. Set condition Functions =============================")
# ============================= 9. Set condition Functions =============================
set7 = {x for x in range(1, 5) if x % 2 == 0}
print("set7 (even numbers):", set7)

print("\n============================ 10. Set Operators =============================")
# ============================= 10. Set Operators =============================
A = {1, 2, 3}
B = {3, 4, 5}

print("\nSet Operators:")
print("A:", A) 
print("B:", B)
print("Union (A | B):", A | B) # | it is union operator
print("Intersection (A & B):", A & B) # & it is intersection operator
print("Difference (A - B):", A - B) # - it is difference operator
print("Symmetric Difference (A ^ B):", A ^ B) # ^ it is symmetric difference operator

print("\n============================ 11. Membership Test =============================")
# ============================= 11. Membership Test =============================
print("\nMembership Test:")
print("2 in A?", 2 in A) # in operator
print("5 not in A?", 5 not in A) # not in operator
