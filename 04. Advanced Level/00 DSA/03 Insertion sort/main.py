"""
  What is Insertion Sort?
  Insertion Sort is a simple, comparison-based, in-place sorting algorithm.
  It builds the sorted array one element at a time by taking an element
  from the unsorted part and inserting it into its correct position
  in the sorted part.

  Core Idea
  The array is conceptually divided into two parts:

  - Sorted subarray — elements already sorted (on the left).
  - Unsorted subarray — remaining elements that still need to be sorted (on the right).

  In each pass:
  1. Take the first element from the unsorted subarray.
  2. Store it in a variable called item.
  3. Compare item with elements in the sorted subarray.
  4. Shift larger elements one position to the right.
  5. Insert item into its correct position.
  6. Extend the sorted subarray by one position.

  This process continues until the entire array is sorted.


  Algorithm (Step-by-Step)
  Given an array A of size n:

  1. Start from index 1 because the first element is already considered sorted.
  2. Set item = A[i].
  3. Set pos = i - 1.
  4. While pos >= 0 and A[pos] > item:
      - Move A[pos] one position to the right.
      - Decrease pos by 1.
  5. Insert item at A[pos + 1].
  6. Repeat until i reaches n - 1.


  Pseudocode

  INSERTION-SORT(A):
      n = length(A)

      for i = 1 to n - 1:
          item = A[i]
          pos = i - 1

          while pos >= 0 and A[pos] > item:
              A[pos + 1] = A[pos]
              pos = pos - 1

          A[pos + 1] = item


  Python Implementation

  class InsertionSort:
      # Python program for implementation of Insertion Sort

      def insertion_sort(self, arr):
          n = len(arr)
          shifts = 0

          for i in range(1, n):

              # Store the current element
              item = arr[i]

              # Position of the previous element
              pos = i - 1

              # Shift larger elements to the right
              while pos >= 0 and arr[pos] > item:
                  arr[pos + 1] = arr[pos]
                  pos -= 1
                  shifts += 1

              # Insert item into its correct position
              arr[pos + 1] = item

              print(f"After pass {i}: {arr} " f"(shifts: {shifts})")

          return arr


  Example Walkthrough

  Initial array:

  [64, 34, 25, 12, 22, 11, 90]


  Pass 1

  Sorted part:
  [64]

  Unsorted part:
  [34, 25, 12, 22, 11, 90]

  item = 34
  pos = 0

  Compare:
  64 > 34

  Shift 64 to the right:

  [64, 64, 25, 12, 22, 11, 90]

  pos = -1

  Insert item at pos + 1:

  [34, 64, 25, 12, 22, 11, 90]


  Pass 2

  Sorted part:
  [34, 64]

  Unsorted part:
  [25, 12, 22, 11, 90]

  item = 25
  pos = 1

  Compare:
  64 > 25
  Shift 64:

  [34, 64, 64, 12, 22, 11, 90]

  pos = 0

  Compare:
  34 > 25
  Shift 34:

  [34, 34, 64, 12, 22, 11, 90]

  pos = -1

  Insert 25:

  [25, 34, 64, 12, 22, 11, 90]


  Pass 3

  Sorted part:
  [25, 34, 64]

  Unsorted part:
  [12, 22, 11, 90]

  item = 12
  pos = 2

  Compare:
  64 > 12
  Shift 64

  34 > 12
  Shift 34

  25 > 12
  Shift 25

  Insert 12:

  [12, 25, 34, 64, 22, 11, 90]


  Pass 4

  Sorted part:
  [12, 25, 34, 64]

  Unsorted part:
  [22, 11, 90]

  item = 22
  pos = 3

  Compare:
  64 > 22
  Shift 64

  34 > 22
  Shift 34

  25 > 22
  Shift 25

  12 < 22
  Stop shifting.

  Insert 22:

  [12, 22, 25, 34, 64, 11, 90]


  Pass 5

  Sorted part:
  [12, 22, 25, 34, 64]

  Unsorted part:
  [11, 90]

  item = 11
  pos = 4

  Compare:
  64 > 11
  Shift 64

  34 > 11
  Shift 34

  25 > 11
  Shift 25

  22 > 11
  Shift 22

  12 > 11
  Shift 12

  Insert 11:

  [11, 12, 22, 25, 34, 64, 90]


  Pass 6

  Sorted part:
  [11, 12, 22, 25, 34, 64]

  Unsorted part:
  [90]

  item = 90
  pos = 5

  Compare:
  64 > 90 → False

  No shifting is required.

  Insert 90 at its current position:

  [11, 12, 22, 25, 34, 64, 90]


  Final sorted array:

  [11, 12, 22, 25, 34, 64, 90]


  Number of Comparisons

  The number of comparisons depends on the input order.


  Best Case

  When the array is already sorted:

  [11, 12, 22, 25, 34, 64, 90]

  Each item only needs one comparison with the previous element.

  Total comparisons:

  n - 1

  Time Complexity:

  O(n)


  Worst Case

  When the array is sorted in reverse order:

  [90, 64, 34, 25, 22, 12, 11]

  Every item must be compared with all elements
  in the sorted portion.

  Total comparisons:

  1 + 2 + 3 + ... + (n - 1)

  = n(n - 1) / 2

  Time Complexity:

  O(n²)


  Average Case

  On average, each item moves through approximately
  half of the sorted portion.

  Time Complexity:

  O(n²)


  Time Complexity

  - Best case: O(n)
  - Average case: O(n²)
  - Worst case: O(n²)

  Important:

  Insertion Sort is different from Selection Sort because
  Insertion Sort can take advantage of an already sorted
  or nearly sorted array.


  Space Complexity

  - Space: O(1)

  Insertion Sort is an in-place sorting algorithm.

  It only uses a few extra variables:

  - i
  - item
  - pos
  - shifts

  Therefore, auxiliary space is O(1).


  Number of Shifts

  Insertion Sort mainly performs shifts instead of swaps.

  Best case:

  0 shifts

  Worst case:

  n(n - 1) / 2 shifts


  Advantages

  - Very easy to understand and implement.
  - In-place sorting algorithm.
  - Requires O(1) extra space.
  - Stable sorting algorithm.
  - Efficient for small arrays.
  - Very efficient for nearly sorted arrays.
  - Can sort data while new elements arrive.
  - Usually performs well when the array is almost sorted.


  Disadvantages

  - Inefficient for large datasets.
  - Average-case time complexity is O(n²).
  - Worst-case time complexity is O(n²).
  - Not suitable for large random datasets when performance matters.


  Stability

  - Insertion Sort is stable by default.

  The condition is:

      arr[pos] > item

  Notice that we use > instead of >=.

  Because equal elements are not shifted, their relative
  order remains unchanged.


  Example:

  [2a, 2b, 1]

  After sorting:

  [1, 2a, 2b]

  2a remains before 2b.

  Therefore, Insertion Sort is stable.


  When to Use Insertion Sort

  - Small datasets.
  - Nearly sorted arrays.
  - When stable sorting is required.
  - When memory usage must be minimal.
  - When O(1) extra space is required.
  - When data arrives one element at a time.
  - Educational purposes.


  When NOT to Use Insertion Sort

  - Very large datasets.
  - Large random arrays.
  - When O(n log n) performance is required.

  Better alternatives include:

  - Merge Sort
  - Quick Sort
  - Heap Sort


  Variants / Notes

  1. Ascending Order

     Select smaller values by using:

         arr[pos] > item


  2. Descending Order

     Change the comparison to:

         arr[pos] < item


  3. Stable Sorting

     Keep:

         arr[pos] > item

     Do not use:

         arr[pos] >= item

     because equal elements should not be shifted.


  4. Online Algorithm

     Insertion Sort can process elements one at a time.

     This makes it useful when new data arrives continuously.


  Selection Sort vs Insertion Sort

  Selection Sort:

  - Best: O(n²)
  - Average: O(n²)
  - Worst: O(n²)
  - Stable: No
  - In-place: Yes
  - Swaps: At most n - 1
  - Good when writes/swaps are expensive


  Insertion Sort:

  - Best: O(n)
  - Average: O(n²)
  - Worst: O(n²)
  - Stable: Yes
  - In-place: Yes
  - Extra space: O(1)
  - Uses shifts instead of repeated swaps
  - Excellent for nearly sorted arrays


  Final Sorted Array

  Input:

  [64, 34, 25, 12, 22, 11, 90]

  Output:

  [11, 12, 22, 25, 34, 64, 90]

"""


class InsertionSort:
    # Python program for implementation of Insertion Sort

    def insertion_sort(self, arr):
        n = len(arr)
        shifts = 0

        for i in range(1, n):

            # Store the current element
            item = arr[i]

            # Position of the previous element
            pos = i - 1

            # Shift larger elements to the right
            while pos >= 0 and arr[pos] > item:
                arr[pos + 1] = arr[pos]
                pos -= 1
                shifts += 1

            # Insert item into its correct position
            arr[pos + 1] = item

            print(f"After pass {i}: {arr} " f"(shifts: {shifts})")

        return arr


if __name__ == "__main__":
    insertion_sort = InsertionSort()

    arr = [64, 34, 25, 12, 22, 11, 90]

    print(f"Original array: {arr}")

    print(
        f"Insertion Sort result: "
        f"{insertion_sort.insertion_sort(arr)}"
    )


class InsertionSort:

    def insertion_sort(self, arr):
        n = len(arr)
        shifts = 0

        for i in range(1, n):
            key = arr[i]

            for j in range(i - 1, -1, -1):
                if arr[j] > key:
                    arr[j + 1] = arr[j]
                    shifts += 1
                else:
                    break

            arr[j + 1] = key

            print(f"After pass {i}: {arr} " f"(shifts: {shifts})")

        return arr


if __name__ == "__main__":
    insertion_sort = InsertionSort()

    arr = [64, 34, 25, 12, 22, 11, 90]

    print(f"Original array: {arr}")
    print(
        f"Insertion Sort result: "
        f"{insertion_sort.insertion_sort(arr)}"
    )