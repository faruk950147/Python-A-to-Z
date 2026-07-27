'''
    Time and Space Complexity

    Time Complexity
    Time Complexity measures how the execution time of an algorithm grows as the input size (n) increases.
    It does not measure the actual time in seconds; instead, it describes the growth rate.


    Example:

    for i in range(n):
        print(i)
    Number of operations: n
    Time Complexity: O(n)

    Space Complexity
    Space Complexity measures how much extra memory an algorithm requires as the input size (n) increases.

    Example:

    arr = [0] * n
    The array stores n elements.
    Space Complexity: O(n)

    If an algorithm only uses a few variables regardless of input size:

    a = 10
    b = 20
    c = a + b
    Space Complexity: O(1) (constant memory)
    Common Time Complexities
    Complexity	Name	Example
    O(1)	Constant	Accessing an array element
    O(log n)	Logarithmic	Binary Search
    O(n)	Linear	Traversing an array
    O(n log n)	Linearithmic	Merge Sort, Heap Sort
    O(n²)	Quadratic	Nested loops, Bubble Sort
    O(2ⁿ)	Exponential	Recursive Fibonacci
    O(n!)	Factorial	Generating all permutations
'''
'''
    # ============================== Time Complexity Examples ==============================
    class TimeComplexityExamples:
        """Class to demonstrate different time complexities"""
        
        def constant_time_example(self, arr):
            """O(1) - Constant Time"""
            return arr[0]  # Always takes same time, regardless of array size

        def linear_time_example(self, arr):
            """O(n) - Linear Time"""
            total = 0
            for num in arr:  # Scales directly with input size
                total += num
            return total

        def quadratic_time_example(self, arr):
            """O(n²) - Quadratic Time"""
            count = 0
            for i in arr:  # Nested loops = n * n = n²
                for j in arr:
                    if i == j:
                        count += 1
            return count
        
    # ============================== Space Complexity Examples ==============================
    class SpaceComplexityExamples:
        """Class to demonstrate different space complexities"""
        
        def constant_space_example(self, n):
            """O(1) - Constant Space"""
            a = 10
            b = 20
            c = a + b
            return c
        
        def linear_space_example(self, n):
            """O(n) - Linear Space"""
            arr = [0] * n
            return arr
        
        def quadratic_space_example(self, n):
            """O(n²) - Quadratic Space"""
            matrix = [[0] * n for _ in range(n)]
            return matrix

'''

# ==================================== Time Complexity Examples ====================================
import time

n = 2**20
start_time = time.time()
for i in range(n):
    print(i, end=" ")
end_time = time.time()
print(f"\nTime taken: {end_time - start_time} seconds")
# ==================================== Space Complexity Examples ====================================
