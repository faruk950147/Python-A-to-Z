import numpy as np

# iteration
arr = np.array([[1, 2, 3], [4, 5, 6]])
print("================== Using for loop index =====================")
for i in range(len(arr)):
    print(f'i is an index {i}, arr[i] is a value {arr[i]}')
print("\n================== Using enumerate =====================")
for i, x in enumerate(arr):
    print(f'i is an index {i}, x is a value {x}')

print("\n================== Using for loop =====================")
for x in arr:
    print(f'x is a value {x}')
print("\n================== Using nditer =====================")
for x in np.nditer(arr):
    print(f'x is a value {x}')
    
print("\n================== Using nditer with step =====================")
for i, x in enumerate(arr):
    print(f'i is an index {i}, x is a value {x}')