# ===================== what is slice =====================

# slice is a built-in function that returns a slice object, 
# which can be used to extract a portion of a sequence (e.g., a string, list, or tuple).

# slice(start, stop, step)

# slice(start, stop)

# slice(stop)

# ===================== positive and negative index =====================

# positive index is the index of an element in a sequence, starting from 0 for the first element. and stop is the index of the element after the last element to be extracted.

# negative index is the index of an element in a sequence, starting from -1 for the last element. and stop is the index of the element after the last element to be extracted.

# ===================== step =====================

# step is the number of elements to skip between each element to be extracted.

# step can be positive or negative.

# if step is positive, the slice will extract elements from left to right.

# if step is negative, the slice will extract elements from right to left.

# ===================== positive slice =====================

# positive slice is a slice that extracts elements from left to right.

str = "hello world"

# str = "hello world"
#        0    1    2    3    4    5    6    7    8    9   10
#       -11   -10  -9   -8   -7   -6   -5   -4   -3   -2  -1
print(len(str))

# ===================== negative slice =====================
# negative slice is a slice that extracts elements from right to left.


# str = "hello world"
#        0    1    2    3    4    5    6    7    8    9   10
#       -11   -10  -9   -8   -7   -6   -5   -4   -3   -2  -1

print(str[2:5])
# Output: llo
print(str[-5:-2])
# Output: orl