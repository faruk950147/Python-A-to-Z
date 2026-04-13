# =========================
# Python List Methods & Functions (Clean Notes)
# =========================

# ---------- 1D List ----------
nums = [1, 2, 3]

print("\n--- 1D LIST ---")

nums.append(4)                # add at end
nums.extend([5, 6])           # add multiple elements
nums.insert(2, 99)            # insert at index
nums.remove(99)               # remove by value
nums.pop(0)                   # remove by index (default last)

print("list:", nums)

print("len:", len(nums))                 # length
print("index(3):", nums.index(3))        # index of value
print("count(2):", nums.count(2))        # frequency

copy1 = nums.copy()                      # shallow copy
print("copy:", copy1)

nums.sort()                               # ascending sort (in-place)
print("sort:", nums)

nums.reverse()                            # reverse list (in-place)
print("reverse:", nums)

print("max:", max(nums))                  # maximum value
print("min:", min(nums))                  # minimum value
print("sum:", sum(nums))                  # sum of elements
print("sorted:", sorted(nums))            # new sorted list

print("any:", any(nums))                  # True if any element is True
print("all:", all(nums))                  # True if all elements are True

for i, v in enumerate(nums):             # index + value
    print("enum:", i, v)

print("zip:", list(zip([1,2,3], ['a','b','c'])))  # combine lists
print("list(str):", list("abc"))                  # string → list


# ---------- 2D List ----------
matrix = [[1, 2, 3], [4, 5, 6]]

print("\n--- 2D LIST ---")

matrix.append([7, 8, 9])         # add row
matrix.extend([[10, 11, 12]])    # add multiple rows
matrix.insert(1, [99, 100, 101]) # insert row
matrix.remove([4, 5, 6])         # remove row
matrix.pop(0)                    # remove row
matrix[0].append(999)            # modify inside row

print("matrix:", matrix)

print("len (rows):", len(matrix))
print("count row:", matrix.count([7,8,9]))

flat = [x for row in matrix for x in row]

print("flatten:", flat)
print("max:", max(flat))
print("min:", min(flat))
print("sum:", sum(flat))
print("sorted:", sorted(flat))


# ---------- 3D List ----------
cube = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]

print("\n--- 3D LIST ---")

cube.append([[9, 10], [11, 12]])
cube.extend([[[13, 14]]])
cube.insert(1, [[99, 100]])
cube.remove([[5, 6], [7, 8]])
cube.pop(0)

cube[0][0].append(999)

print("cube:", cube)

print("len (blocks):", len(cube))
print("len (rows):", len(cube[0]))
print("len (cols):", len(cube[0][0]))

flat3D = [x for block in cube for row in block for x in row]

print("flatten3D:", flat3D)
print("max:", max(flat3D))
print("min:", min(flat3D))
print("sum:", sum(flat3D))
print("sorted:", sorted(flat3D))