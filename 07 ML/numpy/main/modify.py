
import numpy as np

a = np.array([1, 2, 3, 4, 5, 6])
a[3] = 100  # change the 4th element (index 3)
print(a)
# Output: [  1   2   3 100   5   6]

a = np.array([1, 2, 3, 4, 5, 6])
indices = [1, 3, 5]       # 2nd, 4th, 6th elements
a[indices] = [20, 40, 60]
print(a)
# Output: [ 1 20  3 40  5 60]

a = np.array([1, 2, 3, 4, 5, 6])
a[::2] = 0    # change every other element (even indices) to 0
print(a)
# Output: [0 2 0 4 0 6]

a = np.array([1, 2, 3, 4, 5, 6])
a[a % 2 == 0] = 0   # set all even numbers to 0
print(a)
# Output: [1 0 3 0 5 0]

a = np.array([1, 2, 3, 4, 5, 6])
a = np.where(a > 3, 100, a)  # if element > 3 → 100, else keep same
print(a)
# Output: [  1   2   3 100 100 100]

nums = np.array([1, 2, 3, 4, 5, 6])
print("array:", nums)
# array: [1 2 3 4 5 6]


# Adding elements

# Unlike lists, NumPy arrays don’t have append in-place; you use np.append or np.insert which return a new array:

nums = np.append(nums, 7)          # append 7
nums = np.append(nums, [8, 9])     # append multiple
nums = np.insert(nums, 2, 99)      # insert 99 at index 2
print("after adding:", nums)
# after adding: [ 1  2 99  3  4  5  6  7  8  9]


# Removing elements

# No direct remove like lists; use boolean masking or np.delete:

nums = np.delete(nums, 2)  # delete element at index 2
print("after delete index 2:", nums)
# after delete index 2: [1 2 3 4 5 6 7 8 9]

# Accessing and modifying elements
nums[0] = 10         # change first element
nums[1:4] = [20,30,40]  # slice assignment
print("modified:", nums)
# modified: [10 20 30 40 5 6 7 8 9]

# Array functions (equivalent to max, min, sum, etc.)
print("len:", nums.size)       # number of elements
print("max:", np.max(nums))
print("min:", np.min(nums))
print("sum:", np.sum(nums))
print("mean:", np.mean(nums))
print("sorted:", np.sort(nums))  # returns new sorted array
print("any > 0:", np.any(nums > 0))
print("all > 0:", np.all(nums > 0))
# Sorting and reversing
nums_sorted = np.sort(nums)    # returns a new sorted array
nums[::-1]                     # reverse array using slicing
# Copying arrays
copy1 = nums.copy()  # makes a separate copy
# Enumerating and combining arrays

# enumerate() works the same:

for i, v in enumerate(nums):
    print(i, v)

# zip equivalent → np.stack or np.column_stack:

a = np.array([1,2,3])
b = np.array([4,5,6])
c = np.column_stack((a,b))
print(c)
# [[1 4]
#  [2 5]
#  [3 6]]
# Key differences from Python lists:
# Python list	NumPy array
# append(), extend() modifies list in-place	np.append() returns new array
# remove()	np.delete() returns new array
# Dynamic size	Fixed-size (new array must be created to change size)
# Works with mixed types	Optimized for numbers (same dtype)
# Built-in sum(), max()	NumPy functions: np.sum(), np.max()


