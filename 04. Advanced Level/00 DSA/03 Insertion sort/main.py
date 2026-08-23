"""
  What is Insertion Sort?
  Insertion Sort is a simple, comparison-based, in-place sorting algorithm.
  It builds the sorted array one element at a time by taking each element
  from the unsorted portion and inserting it into its correct position
  in the sorted portion.

  Core Idea
  The array is conceptually divided into two parts:

  - Sorted subarray — elements on the left that are already sorted.
  - Unsorted subarray — remaining elements on the right.

  In each pass:
  1. Take the first element from the unsorted portion.
  2. Compare it with elements in the sorted portion.
  3. Shift larger elements one position to the right.
  4. Insert the current element into its correct position.

  This process continues until the entire array is sorted.

  Algorithm (Step-by-Step)
  Given an array A of size n:

  1. Start from index 1 because the first element is considered sorted.
  2. Store A[i] in a variable called key.
  3. Set j = i - 1.
  4. While j >= 0 and A[j] > key:
      - Shift A[j] one position to the right.
      - Decrement j.
  5. Insert key at A[j + 1].
  6. Repeat until all elements are processed.

  Pseudocode

  INSERTION-SORT(A):
      n = length(A)

      for i = 1 to n - 1:
          key = A[i]
          j = i - 1

          while j >= 0 and A[j] > key:
              A[j + 1] = A[j]
              j = j - 1

          A[j + 1] = key

  Python Implementation

  class InsertionSort:

      def insertion_sort(self, arr):
          n = len(arr)
          shifts = 0

          for i in range(1, n):
              # Current element that needs to be inserted
              key = arr[i]

              # Start comparing with the previous element
              j = i - 1

              # Shift elements that are greater than key
              while j >= 0 and arr[j] > key:
                  arr[j + 1] = arr[j]
                  j -= 1
                  shifts += 1

              # Insert key into its correct position
              arr[j + 1] = key

              print(
                  f"After pass {i}: {arr} "
                  f"(shifts: {shifts})"
              )

          return arr


  Example Walkthrough

  Initial array:
  [64, 34, 25, 12, 22, 11, 90]

  Pass 1
  - Sorted part: [64]
  - Key = 34
  - Compare 34 with 64
  - 64 > 34, so shift 64 to the right
  - Insert 34

    → [34, 64, 25, 12, 22, 11, 90]

  Pass 2
  - Sorted part: [34, 64]
  - Key = 25
  - 64 > 25 → shift 64
  - 34 > 25 → shift 34
  - Insert 25

    → [25, 34, 64, 12, 22, 11, 90]

  Pass 3
  - Sorted part: [25, 34, 64]
  - Key = 12
  - 64 > 12 → shift
  - 34 > 12 → shift
  - 25 > 12 → shift
  - Insert 12

    → [12, 25, 34, 64, 22, 11, 90]

  Pass 4
  - Sorted part: [12, 25, 34, 64]
  - Key = 22
  - 64 > 22 → shift
  - 34 > 22 → shift
  - 25 > 22 → shift
  - 12 < 22 → stop
  - Insert 22

    → [12, 22, 25, 34, 64, 11, 90]

  Pass 5
  - Sorted part: [12, 22, 25, 34, 64]
  - Key = 11
  - 64 > 11 → shift
  - 34 > 11 → shift
  - 25 > 11 → shift
  - 22 > 11 → shift
  - 12 > 11 → shift
  - Insert 11

    → [11, 12, 22, 25, 34, 64, 90]

  Pass 6
  - Sorted part: [11, 12, 22, 25, 34, 64]
  - Key = 90
  - 64 < 90 → no shifting required
  - 90 is already in the correct position

    → [11, 12, 22, 25, 34, 64, 90]

  Final sorted array:
  [11, 12, 22, 25, 34, 64, 90]


  Number of Comparisons

  The number of comparisons depends on the input order.

  Best Case:
  Array is already sorted.

  Example:
  [11, 12, 22, 25, 34, 64, 90]

  Only one comparison is needed for each element.

  Comparisons ≈ n - 1

  Time = O(n)


  Worst Case:
  Array is sorted in reverse order.

  Example:
  [90, 64, 34, 25, 22, 12, 11]

  Every new element must be compared with all elements
  in the sorted portion.

  Total comparisons:

  1 + 2 + 3 + ... + (n - 1)

  = n(n - 1) / 2

  Time = O(n²)


  Average Case:
  On average, elements need to move about halfway through
  the sorted portion.

  Time = O(n²)


  Time Complexity

  - Best case: O(n)
  - Average case: O(n²)
  - Worst case: O(n²)

  Unlike Selection Sort, Insertion Sort can take advantage of
  an already sorted or nearly sorted array.


  Space Complexity

  - Space: O(1)

  Insertion Sort works in-place and requires only a few extra
  variables such as key, i, and j.


  Number of Shifts

  Insertion Sort does not usually swap elements.

  Instead, it shifts larger elements to the right and then
  inserts the key into its correct position.

  - Best case: 0 shifts
  - Worst case: n(n - 1) / 2 shifts


  Advantages

  - Very easy to understand and implement.
  - In-place: O(1) extra space.
  - Stable sorting algorithm.
  - Efficient for small datasets.
  - Very efficient for nearly sorted arrays.
  - Can sort data as it arrives (online algorithm).
  - Usually performs well for small or nearly sorted data.


  Disadvantages

  - Inefficient for large datasets.
  - Average and worst-case time complexity is O(n²).
  - Not suitable when the dataset is very large.


  Stability

  - Insertion Sort is stable by default.

  Equal elements maintain their relative order because
  the algorithm shifts elements only when:

      arr[j] > key

  and NOT when:

      arr[j] >= key


  Example:

  [2a, 2b, 1]

  After sorting:

  [1, 2a, 2b]

  The relative order of 2a and 2b remains unchanged.


  When to Use Insertion Sort

  - Small datasets.
  - Nearly sorted arrays.
  - When stability is required.
  - When memory usage must be O(1).
  - When data arrives one element at a time.
  - Educational purposes.


  When NOT to Use Insertion Sort

  - Very large random datasets.
  - When O(n log n) performance is required.

  In those cases, consider:
  - Merge Sort
  - Quick Sort
  - Heap Sort


  Selection Sort vs Insertion Sort

  Selection Sort:
  - Best: O(n²)
  - Average: O(n²)
  - Worst: O(n²)
  - Stable: No
  - Swaps: At most n - 1
  - Good when writes/swaps are expensive

  Insertion Sort:
  - Best: O(n)
  - Average: O(n²)
  - Worst: O(n²)
  - Stable: Yes
  - Very good for nearly sorted data
  - Uses shifts instead of repeated swaps


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
            # Current element that needs to be inserted
            key = arr[i]

            # Start comparing with the previous element
            j = i - 1

            # Shift elements greater than key to the right
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
                shifts += 1

            # Insert key into its correct position
            arr[j + 1] = key

            print(f"After pass {i}: {arr} "
                f"(shifts: {shifts})"
            )

        return arr


if __name__ == "__main__":
    insertion_sort = InsertionSort()

    arr = [64, 34, 25, 12, 22, 11, 90]

    print(f"Original array: {arr}")
    print(f"Insertion Sort result: " f"{insertion_sort.insertion_sort(arr)}")
    
    
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