fruit = ['apple', 'banana', 'cherry']
target = 'banana'

for i in range(len(fruit)):
    if fruit[i] == target:
        print(i)
        break
    else:
        print("Not found")
      
      
# 0 is last index of list
lst = [1,2,3,4,5, 0]
        
for i in range(len(lst)):
    if i == len(lst) - 1:
        print(f"{lst[i]} is at index {i}")
        break
    else:
        print("Not found")
