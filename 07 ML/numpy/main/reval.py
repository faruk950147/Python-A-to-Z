import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])
print('Original Array \n:', arr)

reshaped_arr = arr.reshape(2, 3)
print('Reshaped Array \n:', reshaped_arr)

reval_arr = arr.ravel()
print('Reval Array \n:', reval_arr)