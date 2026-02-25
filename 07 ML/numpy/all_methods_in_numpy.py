# Array Creation Methods
import numpy as np
# Basic Creation                description
np.array()                        # Create array from list
np.zeros()                        # Array of zeros thats all elements are 0
np.ones()                         # Array of ones thats all elements are 1
np.empty()                        # Array with uninitialized values thats all elements are random
np.full()                         # Array filled with specific value
# Range Based
np.arange()                       # Array with range
np.linspace()                     # Array with linear space
np.logspace()                     # Array with log space
# Identity & Diagonal
np.eye()                          # Identity matrix
np.identity()                     # Identity matrix
np.diag()                         # Diagonal matrix
# Random Array
np.random.rand()                  # Random array
np.random.randn()                 # Random array with normal distribution
np.random.randint()               # Random array with integers
np.random.choice()                # Random array with choice
np.random.shuffle()               # Random array with shuffle
# Array Attributes (Properties)
arr.shape                         # Shape of array
arr.ndim                          # Number of dimensions
arr.size                          # Total number of elements
arr.dtype                         # Data type
arr.itemsize                      # Size of each element
# Reshaping & Changing Shape
arr.reshape()                     # Reshape array
arr.flatten()                     # Flatten array
arr.ravel()                       # Flatten array
arr.resize()                      # Resize array
np.expand_dims()                  # Expand dimensions
np.squeeze()                      # Squeeze dimensions
np.transpose()                    # Transpose array
arr.T                             # Transpose array
# Mathematical Operations
# Basic Math
np.add()                          # Addition
np.subtract()                     # Subtraction
np.multiply()                     # Multiplication
np.divide()                       # Division
np.power()                        # Power
np.mod()                          # Modulo
# Rounding
np.round()                        # Round array
np.floor()                        # Floor array
np.ceil()                         # Ceil array
# Exponential & Log
np.exp()                          # Exponential
np.log()                          # Logarithm
np.log10()                        # Logarithm base 10
np.sqrt()                         # Square root
# Statistical Functions
np.mean()                         # Mean
np.median()                       # Median
np.std()                          # Standard deviation
np.var()                          # Variance
np.min()                          # Minimum
np.max()                          # Maximum
np.sum()                          # Sum
np.prod()                         # Product
np.argmin()                       # Index of minimum
np.argmax()                       # Index of maximum
np.percentile()                   # Percentile
# Searching & Sorting
np.sort()                         # Sort array
np.argsort()                      # Sort indices
np.where()                        # Where condition
np.searchsorted()                 # Search sorted
np.unique()                       # Unique elements
# Joining & Splitting Arrays
# Join
np.concatenate()                  # Concatenate arrays
np.vstack()                       # Stack arrays vertically
np.hstack()                       # Stack arrays horizontally
np.stack()                        # Stack arrays
np.column_stack()                 # Column stack
# Split
np.split()                        # Split array
np.vsplit()                       # Split vertically
np.hsplit()                       # Split horizontally
np.array_split()                  # Array split
# Linear Algebra (Very Important)
np.dot()                          # Dot product
np.matmul()                       # Matrix multiplication
np.inner()                        # Inner product
np.outer()                        # Outer product
np.linalg.inv()                   # Matrix inverse
np.linalg.det()                   # Matrix determinant
np.linalg.eig()                   # Eigenvalues and eigenvectors
np.linalg.solve()                 # Solve linear equations
np.linalg.norm()                  # Matrix norm
# Broadcasting & Indexing
arr[0]                            # First element
arr[:, 1]                         # Second column
arr[1:5]                          # Slice
arr[arr > 5]                      # Boolean indexing
# File Handling
np.save()                         # Save array to file
np.load()                         # Load array from file
np.savetxt()                      # Save array to text file
np.loadtxt()                      # Load array from text file
# Copy & View
arr.copy()                        # Copy array
arr.view()                        # View array
# Type Conversion
arr.astype()                      # Convert array type
# Advanced Useful Functions
np.clip()                         # Clip array
np.cumsum()                       # Cumulative sum
np.cumprod()                      # Cumulative product
np.diff()                         # Difference
np.intersect1d()                  # Intersect
np.union1d()                      # Union
np.isin()                         # Is in
# Extra (Universal Functions - ufunc)
np.sin()                          # Sine
np.cos()                          # Cosine
np.tan()                          # Tangent
np.abs()                          # Absolute
np.sign()                         # Sign
np.maximum()                      # Maximum
np.minimum()                      # Minimum
# Real Example
import numpy as np

arr = np.array([1,2,3,4,5])

print("Mean:", np.mean(arr))    # Mean
print("Square:", np.square(arr))    # Square
print("Sorted:", np.sort(arr))    # Sorted