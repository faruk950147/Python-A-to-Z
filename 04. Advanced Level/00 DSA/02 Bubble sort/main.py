"""
  What is Bubble Sort?
  Bubble Sort is a simple, comparison-based, in-place sorting algorithm. It repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.

  The name comes from the way larger elements "bubble up" to the end of the list (or smaller elements "rise" to the front, depending on how you view it).

  Core Idea
  - The array is traversed multiple times (passes).
  - In each pass, adjacent pairs are compared:
    - If A[j] > A[j+1] (for ascending order), they are swapped.
  - After each full pass, the largest unsorted element moves to its correct position at the end.
  - The process repeats until a complete pass makes no swaps → the array is sorted.

  Algorithm (Step-by-Step)
  Given an array A of size n:

  1. Repeat:
    - Set a flag swapped = false.
    - For j from 0 to n - 2 (or up to n - i - 2 in optimized versions):
      - If A[j] > A[j+1]:
        - Swap A[j] and A[j+1].
        - Set swapped = true.
    - If swapped == false, stop (array is sorted).
  2. Optionally, reduce the range each pass because the last i elements are already in place after i passes.

  Pseudocode

  Basic version (without early-stop optimization):

  BUBBLE-SORT(A):
      n = length(A)
      for i = 0 to n - 2:
          for j = 0 to n - 2:
              if A[j] > A[j + 1]:
                  swap A[j] and A[j + 1]

  Optimized version (with early termination and reduced range):

  BUBBLE-SORT-OPT(A):
      n = length(A)
      for i = 0 to n - 2:
          swapped = false
          for j = 0 to n - i - 2:
              if A[j] > A[j + 1]:
                  swap A[j] and A[j + 1]
                  swapped = true
          if swapped == false:
              break

  Python Implementation
  class BubbleSort:
      def bubble_sort(self, arr):
      n = len(arr)
      for i in range(n - 1):
          swapped = False
          # Last i elements are already in place
          for j in range(0, n - i - 1):
              if arr[j] > arr[j + 1]:
                  arr[j], arr[j + 1] = arr[j + 1], arr[j]
                  swapped = True
          # If no two elements were swapped, the array is sorted
          if not swapped:
              break
      return arr

  Example Walkthrough

  Initial array:
  [64, 34, 25, 12, 22, 11, 90]

  Pass 1
  Compare adjacent pairs and swap if out of order:

  - (64, 34) → swap → [34, 64, 25, 12, 22, 11, 90]
  - (64, 25) → swap → [34, 25, 64, 12, 22, 11, 90]
  - (64, 12) → swap → [34, 25, 12, 64, 22, 11, 90]
  - (64, 22) → swap → [34, 25, 12, 22, 64, 11, 90]
  - (64, 11) → swap → [34, 25, 12, 22, 11, 64, 90]
  - (64, 90) → no swap

  After Pass 1:
  [34, 25, 12, 22, 11, 64, 90]
  (90 is now in correct position)

  Pass 2
  Ignore last element (already sorted):

  - (34, 25) → swap → [25, 34, 12, 22, 11, 64, 90]
  - (34, 12) → swap → [25, 12, 34, 22, 11, 64, 90]
  - (34, 22) → swap → [25, 12, 22, 34, 11, 64, 90]
  - (34, 11) → swap → [25, 12, 22, 11, 34, 64, 90]
  - (34, 64) → no swap

  After Pass 2:
  [25, 12, 22, 11, 34, 64, 90]
  (64, 90 are now in correct positions)

  Pass 3
  - (25, 12) → swap → [12, 25, 22, 11, 34, 64, 90]
  - (25, 22) → swap → [12, 22, 25, 11, 34, 64, 90]
  - (25, 11) → swap → [12, 22, 11, 25, 34, 64, 90]
  - (25, 34) → no swap

  After Pass 3:
  [12, 22, 11, 25, 34, 64, 90]

  Pass 4
  - (12, 22) → no swap
  - (22, 11) → swap → [12, 11, 22, 25, 34, 64, 90]
  - (22, 25) → no swap

  After Pass 4:
  [12, 11, 22, 25, 34, 64, 90]

  Pass 5
  - (12, 11) → swap → [11, 12, 22, 25, 34, 64, 90]
  - Rest are in order.

  After Pass 5:
  [11, 12, 22, 25, 34, 64, 90]

  Pass 6
  No swaps occur → algorithm stops (with optimized version).

  Final sorted array:
  [11, 12, 22, 25, 34, 64, 90]

  Number of Comparisons

  For an array of n elements (basic version, no early stop):

  - Pass 1: n - 1 comparisons
  - Pass 2: n - 1 comparisons
  - ...
  - Pass n - 1: n - 1 comparisons

  Total comparisons (worst case, basic version):

  (n-1) + (n-1) + ... + (n-1) = (n-1)(n-1) ≈ O(n^2)

  With the optimized version (reducing range each pass):

  - Pass 1: n - 1
  - Pass 2: n - 2
  - ...
  - Pass n - 1: 1

  Total:

  (n-1) + (n-2) + ... + 1 = n(n-1)/2 = O(n^2)

  For n = 7 (optimized, worst case):

  6 + 5 + 4 + 3 + 2 + 1 = 21

  Time Complexity

  - Best case: O(n) with optimization (already sorted array → only one pass, no swaps).
  - Average case: O(n^2)
  - Worst case: O(n^2) (reverse-sorted array)

  Without the early-stop optimization, even the best case is O(n^2).

  Space Complexity

  - Space: O(1)
  - Bubble Sort is in-place; it uses only a constant amount of extra memory (for a temporary variable during swap and a few counters/flags).

  Number of Swaps

  - In the worst case (reverse-sorted array), Bubble Sort performs many swaps:
    - Up to n(n-1)/2 swaps in the basic version.
  - This is generally more swaps than Selection Sort for the same input.

  Advantages

  - Extremely simple to understand and implement.
  - In-place: requires only constant extra memory.
  - Stable: equal elements keep their relative order (since only adjacent swaps are done when strictly out of order).
  - With optimization, can detect an already-sorted array in O(n) time.

  Disadvantages

  - Very inefficient for large datasets due to O(n^2) average and worst-case time.
  - Performs many swaps compared to algorithms like Selection Sort.
  - Much slower in practice than O(n log n) algorithms such as:
    - Merge Sort
    - Quick Sort
    - Heap Sort

  Stability

  - Bubble Sort is stable.
  - It only swaps adjacent elements when they are strictly out of order (>), so equal elements never swap with each other and retain their original relative order.

  When to Use Bubble Sort

  - Educational purposes: excellent for learning the concept of sorting and algorithmic thinking.
  - Very small arrays where simplicity and code clarity matter more than performance.
  - When you need a simple, stable, in-place sort and performance is not critical.

  When NOT to Use Bubble Sort

  - Large datasets (use O(n log n) algorithms instead).
  - Performance-sensitive applications.
  - When you care about the number of swaps (e.g., writing to slow memory), since Bubble Sort can do many swaps.

  Bubble Sort vs Selection Sort (Quick Comparison)

  Aspect              | Bubble Sort                          | Selection Sort
  --------------------|--------------------------------------|------------------------------------
  Basic operation     | Repeatedly swap adjacent elements    | Select min, swap with first unsorted
  Time (best)         | O(n) with optimization               | O(n^2)
  Time (avg/worst)    | O(n^2)                               | O(n^2)
  Space               | O(1)                                 | O(1)
  Stability           | Stable                               | Not stable (by default)
  Number of swaps     | Can be large (up to ~n^2/2)          | At most n-1
  Early termination   | Can detect sorted array early        | Always does full passes

  Final Sorted Array (Example)

  Input:
  [64, 34, 25, 12, 22, 11, 90]

  Output:
  [11, 12, 22, 25, 34, 64, 90]
"""

class BubbleSort:
    def bubble_sort(self, arr):
      n = len(arr)
      for i in range(n - 1):
          is_swapped = False
          sw = 0
          # Last i elements are already in place
          for j in range(0, n - i - 1):
              if arr[j] > arr[j + 1]:
                  arr[j], arr[j + 1] = arr[j + 1], arr[j]
                  is_swapped = True
                  sw += 1 # only count actual swaps
                  
          print(f"After pass {i + 1}: {arr} (swaps: {sw})")
          
          # If no two elements were swapped, the array is sorted
          if not is_swapped:
              break
      return arr
    
if __name__ == "__main__":
    bubble_sort = BubbleSort()
    arr = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original array: {arr}")
    print(f"Sorted array: {bubble_sort.bubble_sort(arr)}")