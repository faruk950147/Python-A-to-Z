"""
  What is Selection Sort?

  Selection Sort is a simple, comparison-based, in-place sorting algorithm.
  It repeatedly selects the smallest element from the unsorted part of
  the array and moves it to the beginning of the unsorted part.

  For descending order, it selects the largest element instead.


  Core Idea

  The array is conceptually divided into two parts:

  - Sorted subarray:
      Elements that are already in their correct position.

  - Unsorted subarray:
      Elements that still need to be processed.


  In each pass:

  1. Find the minimum element in the unsorted subarray.
  2. Store its index in min_index.
  3. Swap it with the first element of the unsorted subarray.
  4. The sorted subarray grows by one position.


  Example:

  [64, 34, 25, 12, 22, 11, 90]
   ↑
  sorted starts here the first element is considered sorted and the rest is unsorted. 
  The first element is assumed to be the minimum, 64, 
  and the algorithm searches for a smaller element in the unsorted part.


  After Pass 1:

  [11, 34, 25, 12, 22, 64, 90]
   ↑
   sorted


  After Pass 2:

  [11, 12, 25, 34, 22, 64, 90]
       ↑
       sorted


  Algorithm (Step-by-Step)

  Given an array A of size n:

  1. Start with i = 0.
  2. Assume A[i] is the minimum element.
  3. Set min_index = i.
  4. Search the remaining unsorted elements.
  5. If a smaller element is found:
       min_index = j
  6. Swap A[i] with A[min_index].
  7. Move i to the next position.
  8. Repeat until the array is sorted.


  Pseudocode

  SELECTION-SORT(A):

      n = length(A)

      for i = 0 to n - 2:

          min_index = i

          for j = i + 1 to n - 1:

              if A[j] < A[min_index]:

                  min_index = j

          if i != min_index:

              swap A[i] and A[min_index]


  Python Implementation

  class SelectionSort:

      def selection_sort(self, arr):
          n = len(arr)
          swap = 0

          for i in range(n - 1):
              min_index = i

              for j in range(i + 1, n):
                  if arr[j] < arr[min_index]:
                      min_index = j

              if i != min_index:
                  arr[i], arr[min_index] = arr[min_index], arr[i]
                  swap += 1

              print(f"After pass {i + 1}: " f"{arr} (swaps: {swap})")

          return arr


  Example Walkthrough

  Initial array:

  [64, 34, 25, 12, 22, 11, 90]


  Pass 1

  Unsorted part:

  [64, 34, 25, 12, 22, 11, 90]

  Assume:

  min_index = 0
  minimum = 64

  Compare:

  34 < 64
  → min_index = 1

  25 < 34
  → min_index = 2

  12 < 25
  → min_index = 3

  22 < 12
  → No

  11 < 12
  → min_index = 5

  90 < 11
  → No

  Minimum = 11
  Minimum index = 5

  Swap:

  64 ↔ 11

  Result:

  [11, 34, 25, 12, 22, 64, 90]

  swaps = 1


  Pass 2

  Sorted part:

  [11]

  Unsorted part:

  [34, 25, 12, 22, 64, 90]

  Minimum = 12

  Minimum index = 3

  Swap:

  34 ↔ 12

  Result:

  [11, 12, 25, 34, 22, 64, 90]

  swaps = 2


  Pass 3

  Sorted part:

  [11, 12]

  Unsorted part:

  [25, 34, 22, 64, 90]

  Minimum = 22

  Minimum index = 4

  Swap:

  25 ↔ 22

  Result:

  [11, 12, 22, 34, 25, 64, 90]

  swaps = 3


  Pass 4

  Sorted part:

  [11, 12, 22]

  Unsorted part:

  [34, 25, 64, 90]

  Minimum = 25

  Minimum index = 4

  Swap:

  34 ↔ 25

  Result:

  [11, 12, 22, 25, 34, 64, 90]

  swaps = 4


  Pass 5

  Sorted part:

  [11, 12, 22, 25]

  Unsorted part:

  [34, 64, 90]

  Minimum = 34

  34 is already in the correct position.

  No swap.

  Result:

  [11, 12, 22, 25, 34, 64, 90]

  swaps = 4


  Pass 6

  Sorted part:

  [11, 12, 22, 25, 34]

  Unsorted part:

  [64, 90]

  Minimum = 64

  64 is already in the correct position.

  No swap.

  Result:

  [11, 12, 22, 25, 34, 64, 90]

  swaps = 4


  Final Sorted Array:

  [11, 12, 22, 25, 34, 64, 90]


  Number of Comparisons

  For an array of n elements:

  Pass 1:

  n - 1 comparisons

  Pass 2:

  n - 2 comparisons

  Pass 3:

  n - 3 comparisons

  ...

  Pass n - 1:

  1 comparison


  Total comparisons:

  (n - 1) + (n - 2) + ... + 2 + 1

  = n(n - 1) / 2


  For n = 7:

  6 + 5 + 4 + 3 + 2 + 1

  = 21 comparisons


  Time Complexity

  Best Case:

  O(n²)

  Even if the array is already sorted, Selection Sort
  still searches the entire unsorted portion to find
  the minimum element.


  Average Case:

  O(n²)


  Worst Case:

  O(n²)


  Therefore:

  Best    = O(n²)
  Average = O(n²)
  Worst   = O(n²)


  Why is Best Case O(n²)?

  Because Selection Sort does not stop early.

  Example:

  [11, 12, 22, 25, 34, 64, 90]

  Even though the array is already sorted, it still performs:

  6 + 5 + 4 + 3 + 2 + 1

  = 21 comparisons.


  Space Complexity

  Space = O(1)

  Selection Sort is an in-place sorting algorithm.

  It uses only a few extra variables:

  - i
  - j
  - min_index
  - swap
  - temporary value during swapping


  Number of Swaps

  Selection Sort performs at most:

  n - 1 swaps

  For n = 7:

  Maximum swaps = 6


  In our example:

  Pass 1 → Swap
  Pass 2 → Swap
  Pass 3 → Swap
  Pass 4 → Swap
  Pass 5 → No swap
  Pass 6 → No swap

  Total swaps = 4


  This is one of the major advantages of Selection Sort.

  It performs fewer swaps than Bubble Sort in many cases.


  Advantages

  - Very easy to understand.
  - Very easy to implement.
  - In-place sorting algorithm.
  - Requires O(1) extra space.
  - Performs at most n - 1 swaps.
  - Useful when writing/swapping data is expensive.
  - Good for educational purposes.
  - Simple control flow.


  Disadvantages

  - O(n²) time complexity in all cases.
  - Not efficient for large datasets.
  - Does not take advantage of an already sorted array.
  - Usually slower than O(n log n) algorithms.
  - Not stable by default.


  Stability

  Selection Sort is NOT stable by default.

  Equal elements can change their relative order because
  of long-distance swaps.


  Example:

  [2a, 2b, 1]

  First minimum:

  1

  Swap 2a with 1:

  [1, 2b, 2a]

  Originally:

  2a came before 2b.

  After sorting:

  2b comes before 2a.

  Therefore, the relative order changed.

  So Selection Sort is not stable by default.


  When to Use Selection Sort

  - Educational purposes.
  - Very small datasets.
  - When simplicity is important.
  - When memory is extremely limited.
  - When the number of swaps should be minimized.
  - When O(1) extra space is required.


  When NOT to Use Selection Sort

  - Large datasets.
  - Performance-sensitive applications.
  - When stable sorting is required.
  - When O(n log n) performance is needed.


  Better Alternatives

  For large datasets, consider:

  - Merge Sort
  - Quick Sort
  - Heap Sort


  Variants / Notes

  1. Descending Order

  For descending order, find the maximum element instead
  of the minimum element.

  Example:

  [64, 34, 25, 12, 22, 11, 90]

  Select maximum:

  90

  Result after first pass:

  [90, 34, 25, 12, 22, 11, 64]


  2. Stable Selection Sort

  Selection Sort can be modified to become stable.

  Instead of directly swapping the minimum element,
  elements can be shifted/rotated.

  However, this increases the complexity of the algorithm.


  Selection Sort vs Bubble Sort vs Insertion Sort

  Selection Sort:

  - Best: O(n²)
  - Average: O(n²)
  - Worst: O(n²)
  - Stable: No
  - In-place: Yes
  - Swaps: At most n - 1


  Bubble Sort:

  - Best: O(n) with optimization
  - Average: O(n²)
  - Worst: O(n²)
  - Stable: Yes
  - In-place: Yes
  - Swaps: Can be O(n²)


  Insertion Sort:

  - Best: O(n)
  - Average: O(n²)
  - Worst: O(n²)
  - Stable: Yes
  - In-place: Yes
  - Excellent for nearly sorted arrays
  - Uses shifts instead of repeated swaps


  Final Sorted Array

  Input:

  [64, 34, 25, 12, 22, 11, 90]

  Output:

  [11, 12, 22, 25, 34, 64, 90]

"""


class SelectionSort:
    # Python program for implementation of Selection Sort

    def selection_sort(self, arr):
        n = len(arr)
        swap = 0

        for i in range(n - 1):
            # Assume current position contains minimum
            min_index = i

            # Search minimum in the unsorted portion
            for j in range(i + 1, n):
                if arr[j] < arr[min_index]:
                    min_index = j

            # Swap only if minimum is not already in place
            if i != min_index:
                arr[i], arr[min_index] = arr[min_index], arr[i]
                swap += 1

            print(f"After pass {i + 1}: " f"{arr} (swaps: {swap})")

        return arr


if __name__ == "__main__":

    selection_sort = SelectionSort()

    arr = [64, 34, 25, 12, 22, 11, 90]

    print(f"Original array: {arr}")

    print(f"Selection Sort result: " f"{selection_sort.selection_sort(arr)}")
    