# =========================
# Python List Methods & Functions
# =========================

# ---------- 1D List ----------
nums = [1, 2, 3]

print("\n--- 1D LIST ---")
nums.append(4)                # append()
nums.extend([5, 6])           # extend()
nums.insert(2, 99)            # insert()
nums.remove(99)               # remove()
nums.pop(0)                   # pop()
print("list:", nums)

print("len:", len(nums))      # len()
print("index(3):", nums.index(3))  # index()
print("count(2):", nums.count(2))  # count()

copy1 = nums.copy()           # copy()
print("copy:", copy1)

nums.sort()                   # sort()
print("sort:", nums)

nums.reverse()                # reverse()
print("reverse:", nums)

print("max:", max(nums))      # max()
print("min:", min(nums))      # min()
print("sum:", sum(nums))      # sum()
print("sorted:", sorted(nums))  # sorted()
print("any:", any(nums))      # any()
print("all:", all(nums))      # all()

for i, v in enumerate(nums):  # enumerate()
    print("enum:", i, v)

print("zip:", list(zip([1,2,3], ['a','b','c'])))  # zip()
print("list(str):", list("abc"))                  # list()


# ---------- 2D List ----------
matrix = [[1, 2, 3], [4, 5, 6]]

print("\n--- 2D LIST ---")
matrix.append([7, 8, 9])         # append row
matrix.extend([[10, 11, 12]])    # extend rows
matrix.insert(1, [99, 100, 101]) # insert row
matrix.remove([4, 5, 6])         # remove row
matrix.pop(0)                    # pop row
matrix[0].append(999)            # append inside row
print("matrix:", matrix)

print("len (rows):", len(matrix))      # len()
print("count [7,8,9]:", matrix.count([7,8,9]))  # count()

# flatten 2D for numerical funcs
flat = [x for row in matrix for x in row]
print("flatten:", flat)
print("max:", max(flat))   # max()
print("min:", min(flat))   # min()
print("sum:", sum(flat))   # sum()
print("sorted:", sorted(flat))  # sorted()


# ---------- 3D List ----------
cube = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]

print("\n--- 3D LIST ---")
cube.append([[9, 10], [11, 12]])  # append block
cube.extend([[[13, 14]]])         # extend block
cube.insert(1, [[99, 100]])       # insert block
cube.remove([[5, 6], [7, 8]])     # remove block
cube.pop(0)                       # pop block
cube[0][0].append(999)            # append inside 3D
print("cube:", cube)

print("len (blocks):", len(cube))         # len()
print("len (rows in block0):", len(cube[0]))  
print("len (cols in block0,row0):", len(cube[0][0]))

# flatten 3D
flat3D = [x for block in cube for row in block for x in row]
print("flatten3D:", flat3D)
print("max:", max(flat3D))   # max()
print("min:", min(flat3D))   # min()
print("sum:", sum(flat3D))   # sum()
print("sorted:", sorted(flat3D))  # sorted()
