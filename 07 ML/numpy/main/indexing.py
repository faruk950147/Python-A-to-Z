import numpy as np

"""
# indexing slicing and dicing one dimentional array
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(f"indexing arr[0]",arr[0])
print(f"indexing arr[1]",arr[1])
# negative indexing
print(f"negative indexing arr[-1]",arr[-1])
print(f"negative indexing arr[-2]",arr[-2])
# range of index
print(f"range of index arr[0:5]",arr[0:5])
print(f"range of index arr[5:10]",arr[5:10])
print(f"range of index arr[0:10]",arr[0:10])
# step
print(f"step arr[0:10:2]",arr[0:10:2])
print(f"step arr[0:10:3]",arr[0:10:3])
# negative step
print(f"negative step arr[10:0:-1]",arr[10:0:-1])
print(f"negative step arr[10:0:-2]",arr[10:0:-2])
print(f"negative step arr[10:0:-3]",arr[10:0:-3])
# range of index
print(f"range of index arr[:2:5]",arr[:2:5])
# range of index
print(f"range of index arr[2:5]",arr[2:5])
print(f"range of index arr[-5:-2]",arr[-5:-2])
# dynamic indexing
print(len(arr) - 1)
print(arr[len(arr) - 1])
"""

def dynamic_indexing(arr):
    # dynamic indexing using numpy
    # len(arr) - 1 → last index
    # arr[len(arr) - 1] → last item
    # return arr[len(arr) - 1] → return last item
    # len(arr) → length of array
    # why len(arr) - 1? this inside of dynamic indexing in python
    arr = np.array(arr)
    if len(arr) > 0:
        return arr[len(arr) - 1]
    return None

print(dynamic_indexing([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))




