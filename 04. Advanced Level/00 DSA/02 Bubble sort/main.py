"""
  What is Bubble Sort?

  Bubble Sort is a simple, comparison-based, in-place sorting algorithm.
  It repeatedly compares adjacent elements and swaps them if they are
  in the wrong order.

  The name "Bubble Sort" comes from the idea that larger elements
  gradually "bubble up" to the end of the array after each pass.


  Core Idea

  The array is traversed multiple times.

  In each pass:

  1. Compare adjacent elements.
  2. If the left element is greater than the right element,
     swap them.
  3. After each pass, the largest unsorted element moves to
     its correct position at the end.
  4. The last i elements are already sorted, so they can be ignored.
  5. If no swap occurs during a complete pass, the array is already sorted.


  Algorithm (Step-by-Step)

  Given an array A of size n:

  1. Start from the first element.
  2. Compare A[j] and A[j + 1].
  3. If A[j] > A[j + 1], swap them.
  4. Continue until the end of the unsorted portion.
  5. After one pass, the largest element reaches the end.
  6. Repeat the process for the remaining unsorted portion.
  7. Stop early if no swap occurs.


  Pseudocode

  BUBBLE-SORT(A):

      n = length(A)

      for i = 0 to n - 2:

          swapped = false

          for j = 0 to n - i - 2:

              if A[j] > A[j + 1]:

                  swap A[j], A[j + 1]

                  swapped = true

          if swapped == false:

              break


  Python Implementation

  class BubbleSort:

      def bubble_sort(self, arr):
          n = len(arr)
          swaps = 0

          for i in range(n - 1):
              is_swapped = False
              pass_swaps = 0

              # Last i elements are already in correct position
              for j in range(0, n - i - 1):
                  if arr[j] > arr[j + 1]:
                      arr[j], arr[j + 1] = arr[j + 1], arr[j]

                      is_swapped = True
                      swaps += 1
                      pass_swaps += 1

              print(f"After pass {i + 1}: " f"{arr} " f"(swaps: {pass_swaps}, total swaps: {swaps})")

              # If no swap occurred, array is already sorted
              if not is_swapped:
                  break

          return arr


  Example Walkthrough

  Initial array:

  [64, 34, 25, 12, 22, 11, 90]


  Pass 1

  Compare adjacent elements:

  64 > 34
  → Swap

  [34, 64, 25, 12, 22, 11, 90]

  64 > 25
  → Swap

  [34, 25, 64, 12, 22, 11, 90]

  64 > 12
  → Swap

  [34, 25, 12, 64, 22, 11, 90]

  64 > 22
  → Swap

  [34, 25, 12, 22, 64, 11, 90]

  64 > 11
  → Swap

  [34, 25, 12, 22, 11, 64, 90]

  64 < 90
  → No swap

  After Pass 1:

  [34, 25, 12, 22, 11, 64, 90]

  90 is now in its correct position.


  Pass 2

  Ignore 90 because it is already sorted.

  34 > 25
  → Swap

  [25, 34, 12, 22, 11, 64, 90]

  34 > 12
  → Swap

  [25, 12, 34, 22, 11, 64, 90]

  34 > 22
  → Swap

  [25, 12, 22, 34, 11, 64, 90]

  34 > 11
  → Swap

  [25, 12, 22, 11, 34, 64, 90]

  34 < 64
  → No swap

  After Pass 2:

  [25, 12, 22, 11, 34, 64, 90]


  Pass 3

  25 > 12
  → Swap

  [12, 25, 22, 11, 34, 64, 90]

  25 > 22
  → Swap

  [12, 22, 25, 11, 34, 64, 90]

  25 > 11
  → Swap

  [12, 22, 11, 25, 34, 64, 90]

  25 < 34
  → No swap

  After Pass 3:

  [12, 22, 11, 25, 34, 64, 90]


  Pass 4

  12 < 22
  → No swap

  22 > 11
  → Swap

  [12, 11, 22, 25, 34, 64, 90]

  22 < 25
  → No swap

  After Pass 4:

  [12, 11, 22, 25, 34, 64, 90]


  Pass 5

  12 > 11
  → Swap

  [11, 12, 22, 25, 34, 64, 90]

  Remaining elements are already sorted.

  After Pass 5:

  [11, 12, 22, 25, 34, 64, 90]


  Pass 6

  No swaps occur.

  Therefore, the algorithm stops early.


  Final sorted array:

  [11, 12, 22, 25, 34, 64, 90]


  Number of Comparisons

  For the optimized version:

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

  Therefore:

  O(n²)


  For n = 7:

  6 + 5 + 4 + 3 + 2 + 1

  = 21 comparisons


  Time Complexity

  Best Case:

  O(n)

  When the array is already sorted and the optimized version
  detects that no swaps occurred.


  Average Case:

  O(n²)


  Worst Case:

  O(n²)

  This happens when the array is in reverse order.


  Important:

  Without the early-stop optimization:

  Best Case = O(n²)

  With early-stop optimization:

  Best Case = O(n)


  Space Complexity

  Space = O(1)

  Bubble Sort is an in-place sorting algorithm.

  It only requires a constant amount of extra memory for:

  - i
  - j
  - is_swapped
  - temporary values during swapping


  Number of Swaps

  Best Case:

  0 swaps

  Already sorted array.


  Worst Case:

  n(n - 1) / 2 swaps

  Reverse-sorted array.


  Advantages

  - Very easy to understand.
  - Very easy to implement.
  - In-place sorting algorithm.
  - Requires O(1) extra space.
  - Stable sorting algorithm.
  - Optimized version can detect an already sorted array.
  - Good for educational purposes.


  Disadvantages

  - Very slow for large datasets.
  - Average time complexity is O(n²).
  - Worst-case time complexity is O(n²).
  - Performs many swaps.
  - Much slower than O(n log n) algorithms.


  Stability

  Bubble Sort is stable.

  The condition is:

      arr[j] > arr[j + 1]

  We do NOT use:

      arr[j] >= arr[j + 1]

  Therefore, equal elements are not swapped.

  Example:

      [2a, 2b, 1]

  After sorting:

      [1, 2a, 2b]

  The relative order of 2a and 2b remains unchanged.


  When to Use Bubble Sort

  - Educational purposes.
  - Very small arrays.
  - When simplicity is more important than performance.
  - When a stable, in-place algorithm is required.
  - When detecting an already sorted array is useful.


  When NOT to Use Bubble Sort

  - Large datasets.
  - Performance-sensitive applications.
  - When O(n log n) performance is required.
  - When the number of swaps should be minimized.


  Better Alternatives

  For large datasets, consider:

  - Merge Sort
  - Quick Sort
  - Heap Sort


  Bubble Sort vs Selection Sort vs Insertion Sort

  Bubble Sort:

  - Best: O(n)
  - Average: O(n²)
  - Worst: O(n²)
  - Stable: Yes
  - In-place: Yes
  - Swaps: Can be O(n²)
  - Good for learning and small data


  Selection Sort:

  - Best: O(n²)
  - Average: O(n²)
  - Worst: O(n²)
  - Stable: No by default
  - In-place: Yes
  - Swaps: At most n - 1
  - Good when swaps are expensive


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


class BubbleSort:
    # Python program for implementation of Bubble Sort

    def bubble_sort(self, arr):
        n = len(arr)
        swaps = 0

        for i in range(n - 1):
            is_swapped = False
            pass_swaps = 0

            # Last i elements are already in correct position
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

                    is_swapped = True
                    swaps += 1
                    pass_swaps += 1

            print(f"After pass {i + 1}: " f"{arr} " f"(swaps: {pass_swaps}, total swaps: {swaps})")

            # If no swap occurred, array is already sorted
            if not is_swapped:
                break

        return arr


if __name__ == "__main__":
    bubble_sort = BubbleSort()

    arr = [64, 34, 25, 12, 22, 11, 90]

    print(f"Original array: {arr}")

    print(
        f"Bubble Sort result: "
        f"{bubble_sort.bubble_sort(arr)}"
    )