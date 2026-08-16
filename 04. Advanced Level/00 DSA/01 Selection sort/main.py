"""
  What is Selection Sort?
  Selection Sort is a simple, comparison-based, in-place sorting algorithm. It repeatedly selects the smallest (or largest, if sorting descending) element from the unsorted part of the array and moves it to the boundary of the sorted part.

  Core Idea
  The array is conceptually divided into two parts:

  - Sorted subarray — elements already in correct order (on the left).
  - Unsorted subarray — remaining elements that still need to be sorted (on the right).

  In each pass:
  1. Find the minimum element in the unsorted subarray.
  2. Swap it with the first element of the unsorted subarray.
  3. Extend the sorted subarray by one position to the right.

  This process continues until the entire array is sorted.

  Algorithm (Step-by-Step)
  Given an array A of size n:

  1. Set i = 0 (start of unsorted part).
  2. While i < n - 1:
    - Assume min_index = i.
    - For each j from i + 1 to n - 1:
      - If A[j] < A[min_index], update min_index = j.
    - Swap A[i] and A[min_index].
    - Increment i by 1 (sorted part grows by one).

  Pseudocode

  SELECTION-SORT(A):
      n = length(A)
      for i = 0 to n - 2:
          min_index = i
          for j = i + 1 to n - 1:
              if A[j] < A[min_index]:
                  min_index = j
          swap A[i] and A[min_index]

  Python Implementation
  class SelectionSort:
    # Python program for implementation of Selection Sort

      def selection_sort(self, arr):
          n = len(arr)
          for i in range(n - 1):
              # Assume the current position holds the minimum element
              min_index = i
              # Iterate through the unsorted portion to find the actual minimum element
              for j in range(i + 1, n):
                  if arr[j] < arr[min_index]:
                      min_index = j
              # Only swap if the minimum element is not already in the correct position
              if i != min_index:
                  arr[i], arr[min_index] = arr[min_index], arr[i]
          return arr

  Example Walkthrough

  Initial array:
  [64, 34, 25, 12, 22, 11, 90]

  Pass 1
  - Search in: [64, 34, 25, 12, 22, 11, 90]
  - Minimum = 11 (at index 5)
  - Swap 64 and 11
    → [11, 34, 25, 12, 22, 64, 90]

  Pass 2
  - Search in: [34, 25, 12, 22, 64, 90]
  - Minimum = 12
  - Swap 34 and 12
    → [11, 12, 25, 34, 22, 64, 90]

  Pass 3
  - Search in: [25, 34, 22, 64, 90]
  - Minimum = 22
  - Swap 25 and 22
    → [11, 12, 22, 34, 25, 64, 90]

  Pass 4
  - Search in: [34, 25, 64, 90]
  - Minimum = 25
  - Swap 34 and 25
    → [11, 12, 22, 25, 34, 64, 90]

  Pass 5
  - Search in: [34, 64, 90]
  - Minimum = 34
  - Already in correct position → no swap
    → [11, 12, 22, 25, 34, 64, 90]

  Pass 6
  - Search in: [64, 90]
  - Minimum = 64
  - Already in correct position → no swap
    → [11, 12, 22, 25, 34, 64, 90]

  Final sorted array:
  [11, 12, 22, 25, 34, 64, 90]

  Number of Comparisons

  For an array of n elements:

  - Pass 1: n - 1 comparisons
  - Pass 2: n - 2 comparisons
  - ...
  - Pass n - 1: 1 comparison

  Total comparisons:

  (n-1) + (n-2) + ... + 2 + 1 = n(n-1)/2

  For n = 7:

  6 + 5 + 4 + 3 + 2 + 1 = 21

  Time Complexity

  - Best case: O(n^2)
  - Average case: O(n^2)
  - Worst case: O(n^2)

  Reason: The algorithm always performs the same number of comparisons regardless of input order; it always scans the unsorted part to find the minimum.

  Space Complexity

  - Space: O(1)
  - It sorts in place using only a constant amount of extra memory (a few variables like min_index, i, j, and a temporary for swapping).

  Number of Swaps

  - At most n - 1 swaps (one per pass).
  - Often fewer than Bubble Sort for the same input, because it swaps only when the minimum is not already in place.

  Advantages

  - Very easy to understand and implement.
  - In-place: requires only constant extra memory.
  - Performs fewer swaps than Bubble Sort, which can be useful when swaps are expensive.

  Disadvantages

  - Inefficient for large datasets due to O(n^2) time.
  - Does not take advantage of existing order; even a sorted array requires O(n^2) comparisons.
  - Slower in practice than more advanced algorithms like:
    - Merge Sort (O(n log n))
    - Quick Sort (average O(n log n))
    - Heap Sort (O(n log n))

  Stability

  - Selection Sort is not stable by default.
  - Equal elements may change relative order due to swaps.
  - Example: if you have [2a, 2b, 1], after sorting you might get [1, 2b, 2a] depending on implementation.

  When to Use Selection Sort

  - Educational purposes: great for learning how sorting works.
  - Very small arrays where simplicity matters more than performance.
  - Situations where:
    - Memory is extremely constrained (in-place is required).
    - Writes/swaps are costly and you want to minimize them.

  When NOT to Use Selection Sort

  - Large datasets (use O(n log n) algorithms instead).
  - When performance matters in real applications.
  - When you need a stable sort and cannot modify the algorithm to ensure stability.

  Variants / Notes

  - Can be adapted to sort in descending order by selecting the maximum element instead of the minimum.
  - Can be made stable with extra care (e.g., using rotations instead of direct swaps), but this usually increases complexity and is rarely done in practice.

  Final Sorted Array (Example)

  Input:
  [64, 34, 25, 12, 22, 11, 90]

  Output:
  [11, 12, 22, 25, 34, 64, 90]


"""

class SelectionSort:
  # Python program for implementation of Selection Sort

    def selection_sort(self, arr):
        n = len(arr)
        sw = 0
        for i in range(n - 1):
            # Assume the current position holds the minimum element
            min_index = i
            # Iterate through the unsorted portion to find the actual minimum element
            for j in range(i + 1, n):
                if arr[j] < arr[min_index]:
                    min_index = j
            # Only swap if the minimum element is not already in the correct position
            if i != min_index:
                arr[i], arr[min_index] = arr[min_index], arr[i]
                sw += 1
            print(f"After pass {i + 1}: {arr} (swaps: {sw})")
        return arr
      
if __name__ == "__main__":
    selection_sort = SelectionSort()
    arr = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original array: {arr}")
    print(f"Selection Sort result: {selection_sort.selection_sort(arr)}")
    