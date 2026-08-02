"""
    Selection Sort

    Selection Sort is a simple sorting algorithm that repeatedly finds the smallest element from the unsorted portion of the array and places it at the beginning.

    The algorithm maintains two parts of the array:

    Sorted subarray - Elements already arranged in order.
    Unsorted subarray - Remaining elements that need to be sorted.

    In each pass, the minimum element from the unsorted subarray is selected and swapped with the first unsorted element.

    Algorithm
    Start from the first element.
    Find the smallest element in the unsorted part of the array.
    Swap it with the first unsorted element.
    Move the boundary of the sorted subarray one position to the right.
    Repeat until the array is completely sorted.
    Example

    Initial array:

    [64, 34, 25, 12, 22, 11, 90]
    Pass 1

    Find the minimum element in the entire array.

    Minimum = 11

    Swap 64 and 11

    [11, 34, 25, 12, 22, 64, 90]
    Pass 2

    Search in:

    [34, 25, 12, 22, 64, 90]

    Minimum = 12

    Swap 34 and 12

    [11, 12, 25, 34, 22, 64, 90]
    Pass 3

    Search in:

    [25, 34, 22, 64, 90]

    Minimum = 22

    Swap 25 and 22

    [11, 12, 22, 34, 25, 64, 90]
    Pass 4

    Search in:

    [34, 25, 64, 90]

    Minimum = 25

    Swap 34 and 25

    [11, 12, 22, 25, 34, 64, 90]
    Pass 5

    Search in:

    [34, 64, 90]

    Minimum = 34

    No swap needed.

    [11, 12, 22, 25, 34, 64, 90]
    Pass 6

    Search in:

    [64, 90]

    Minimum = 64

    No swap needed.

    [11, 12, 22, 25, 34, 64, 90]
    Comparisons in Each Pass

    For an array of 7 elements:

    Pass	Comparisons
    Pass 1	6
    Pass 2	5
    Pass 3	4
    Pass 4	3
    Pass 5	2
    Pass 6	1
    Total	21
    Time Complexity
    Best Case: O(n²)
    Average Case: O(n²)
    Worst Case: O(n²)
    Space Complexity
    O(1) (In-place sorting)
    Advantages
    Easy to understand and implement.
    Requires only constant extra memory.
    Performs fewer swaps than Bubble Sort.
    Disadvantages
    Inefficient for large datasets.
    Time complexity remains O(n²) even if the array is already sorted.
    Generally slower than efficient algorithms like Merge Sort or Quick Sort for large inputs.

    Final Sorted Array:

    [11, 12, 22, 25, 34, 64, 90]
"""
