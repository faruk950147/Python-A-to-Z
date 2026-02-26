
import numpy as np

matrix = np.array(
    [[1, 2, 3],  # Row 1
     [4, 5, 6],  # Row 2
     [7, 8, 9]]  # Row 3
    )

print(f"Matrix Row 1 to 1 \n: {matrix[0:1]}")
print(f"Matrix Row 1 to 2 \n: {matrix[0:2]}")
print(f"Matrix Row 1 to 3 \n: {matrix[0:3]}")
print(f"Matrix Row 1 to 2 and Column 1 to 3 \n: {matrix[0:2, 0:3]}")