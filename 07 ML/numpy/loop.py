import numpy as np

# iteration
arr = np.array([1, 2, 3, 4, 5])
print("================== Using for loop index =====================")
for i in range(len(arr)):
    print(arr[i], end=" ")
print("\n================== Using enumerate =====================")
for i, x in enumerate(arr):
    print(i, x, end=" ")

print("\n================== Using for loop =====================")
for x in arr:
    print(x, end=" ")
print("\n================== Using nditer =====================")
for x in np.nditer(arr):
    print(x, end=" ")
    
print("\n================== Using nditer with step =====================")
for i, x in enumerate(arr):
    print(i, x, end=" ")