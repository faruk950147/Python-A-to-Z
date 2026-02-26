"""
NumPy Ultimate Guide: Memory, Axis, Order, Flags, Reshape & Broadcasting
NumPy Overview

NumPy হলো Python-এর library যা provides:

Arrays (n-dimensional arrays)

Linear Algebra → np.linalg

Fourier Transform → np.fft

Matrix Operations → dot, matmul, inverse, determinant, etc.

Advanced indexing, broadcasting, and reshaping

Memory Layout: order

order decides how array elements are stored in memory.

Value	Meaning
"C"	C-style → Row-major (default)
"F"	Fortran-style → Column-major

Row-major: elements stored row by row

Column-major: elements stored column by column

Note: Printing output stays the same. Only memory layout changes.

"""
import numpy as np

arr_c = np.array([[1,2,3],[4,5,6]], order='C')
arr_f = np.array([[1,2,3],[4,5,6]], order='F')

print(arr_c.flags.c_contiguous)  # True
print(arr_f.flags.f_contiguous)  # True


"""
Axis

Axis determines along which dimension an operation is performed.

For a 2D array:

axis = 0 → operation down the rows → column-wise result

axis = 1 → operation across the columns → row-wise result

"""
arr = np.array([[1,2,3],
                [4,5,6]])

print(arr.sum(axis=0))  # Column-wise sum → [5 7 9]
print(arr.sum(axis=1))  # Row-wise sum → [6 15]

"""
Think of axis as:

axis=0 = vertical (↓) that means column-wise

axis=1 = horizontal (→) that means row-wise

Array Flags: arr.flags

Flags provide memory layout and ownership info.

Flag	Meaning
c_contiguous	True → stored in row-major order
f_contiguous	True → stored in column-major order
owndata	True → array owns its memory
writeable	True → array can be modified
aligned	True → data aligned in memory

"""
arr = np.array([[1,2,3],[4,5,6]], order='C')
print(arr.flags)


"""
Reshape & Adding New Axis
Original 1D Array:
a = np.array([1,2,3,4])
print(a.shape)  # (4,)
Convert to 2D:
Method 1: reshape()
# Column vector
a_col = a.reshape(4,1)
print(a_col)
# [[1]
#  [2]
#  [3]
#  [4]]

# Row vector
a_row = a.reshape(1,4)
print(a_row)
# [[1 2 3 4]]
Method 2: np.newaxis or None
# Column vector
a_col = a[:, np.newaxis]
# or a[:, None]

# Row vector
a_row = a[np.newaxis, :]
# or a[None, :]
Method 3: Automatic reshape with -1
a.reshape(-1,1)  # Column
a.reshape(1,-1)  # Row

Broadcasting & Axis

Broadcasting allows operations on arrays of different shapes.
Axis is important for functions like sum, mean, max:
"""

A = np.array([[1,2,3],[4,5,6]])
B = np.array([10,20,30])

print(A + B)  # Adds B to each row of A


print(A.sum(axis=0))  # Column-wise sum → [5 7 9]
print(A.sum(axis=1))  # Row-wise sum → [6 15]

"""
View vs Copy

View: new array shares same memory (a_view = a.reshape(...))

Copy: new array has its own memory (a_copy = a.copy())

Check with owndata:

print(a.flags.owndata)       # True → owns memory
print(a_view.flags.owndata)  # False → shares memory
print(a_copy.flags.owndata)  # True → independent copy

"""
"""
Summary Table
Concept	Details
order	"C"=row-major, "F"=column-major
axis	axis=0 → down rows (column-wise), axis=1 → across columns (row-wise)
arr.flags.c_contiguous	True → row-major memory
arr.flags.f_contiguous	True → column-major memory
arr.flags.owndata	True → owns memory
reshape() / np.newaxis	Change dimensions / add axes
Broadcasting	Operate on arrays of different shapes
View vs Copy	View shares memory, Copy owns memory

"""
