# Array Creation Methods
import time
import numpy as np   
"""
# From a Python list
print("Time taken to create an array from a Python list using array()")
start_time = time.time()
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(f"Time taken: {time.time() - start_time:.4f} seconds")

# From a Python tuple
print("\nTime taken to create an array from a Python tuple using array()")
start_time = time.time()
arr = np.array((1, 2, 3, 4, 5))
print(arr)
print(f"Time taken: {time.time() - start_time:.4f} seconds")


# From a Python range
print("\nTime taken to create an array from a Python range using array()")
start_time = time.time()
arr = np.array(range(1, 6))
print(arr)
print(f"Time taken: {time.time() - start_time:.4f} seconds")


# From a Python list with different data types
print("\nTime taken to create an array from a Python list with different data types using array()")
start_time = time.time()
arr = np.array([1, 2.0, 3, 4.0, 5])
print(arr)
print(f"Time taken: {time.time() - start_time:.4f} seconds")



# all elements are zeros
print("\nTime taken to create an array with all elements as zeros using zeros()")
start_time = time.time()
arr = np.zeros(5)
print(arr)
print(f"Time taken: {time.time() - start_time:.4f} seconds")

# all elements are ones
print("\nTime taken to create an array with all elements as ones using ones()")
start_time = time.time()
arr = np.ones(5)
print(arr)
print(f"Time taken: {time.time() - start_time:.4f} seconds")

# empty array with uninitialized values
arr = np.empty(5)
print(arr)

# array with random values
print("\nTime taken to create an array with random values using random()")
start_time = time.time()
arr = np.random.random(5)
print(arr)
print(f"Time taken: {time.time() - start_time:.4f} seconds")



# array with random integers
print("\nTime taken to create an array with random integers using randint()")
start_time = time.time()
arr = np.random.randint(1, 10, 5)
print(arr)
print(f"Time taken: {time.time() - start_time:.4f} seconds")


# array with full of specific value
print("\nTime taken to create an array with full of specific value using full()")
start_time = time.time()
arr = np.full(5, 10) # 5 elements with value 10
print(arr)
print(f"Time taken: {time.time() - start_time:.4f} seconds")

start_time = time.time()
arr = np.full([2, 4], 5) # 2 rows and 4 columns
print(arr)
print(f"Time taken: {time.time() - start_time:.4f} seconds")


# all elements are in a range with step even numbers
arr = np.arange(2, 10, 2)
print(arr)


a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('number of dimensions :', arr.ndim)


# accessing 1D array elements
arr = np.array([1, 2, 3, 4])
# first row, first column
print("arr[0]:", arr[0])

# accessing 2D array elements
arr = np.array([[1, 2, 3], [4, 5, 6]])
# first row, first column
print("arr[0, 0]:", arr[0, 0])

# accessing 3D array elements
arr = np.array(
    [
        # layer 0
        [
            [1, 2, 3], 
            [4, 5, 6]
        ], 
        # layer 1
        [
            [1, 2, 3], 
            [4, 5, 6]
        ]
    ]
)
# first row, first column, first element
print("arr[0, 0, 0]:", arr[0, 0, 0])

# reshape thats means old data to new shape
x = np.arange(24).reshape(2, 3, 4)
print(x)
"""
# arr = np.array([1, 2, 3, 4], ndmin=5)
# print(arr)
# print('number of dimensions :', arr.ndim)
