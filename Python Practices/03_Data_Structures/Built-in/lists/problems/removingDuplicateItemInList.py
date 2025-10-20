import numpy as np

# 1st way using set
def remove_duplicate(list1):
    return list(set(list1))

print(remove_duplicate([1, 2, 3, 4, 5, 1, 2, 3, 4, 5]))

# 2nd way using dict
def remove_duplicate_2(list1):
    return list(dict.fromkeys(list1))

print(remove_duplicate_2([1, 2, 3, 4, 5, 1, 2, 3, 4, 5]))

# 3rd way using for loop with range and custom logic
def remove_duplicate_3(list1):
    list2 = []
    for i in range(len(list1)):
        if list1[i] not in list2:
            list2 += [list1[i]]
    return list2

print(remove_duplicate_3([1, 2, 3, 4, 5, 1, 2, 3, 4, 5]))

# 4th way using for loop with custom logic
def remove_duplicate_4(list1):
    list2 = []
    for i in list1:
        if i not in list2:
            list2 += [i]
    return list2

print(remove_duplicate_4([1, 2, 3, 4, 5, 1, 2, 3, 4, 5]))

# 5th way using list comprehension
def remove_duplicate_5(list1):
    return [list1[i] for i in range(len(list1)) if list1[i] not in list1[:i]]

print(remove_duplicate_5([1, 2, 3, 4, 5, 1, 2, 3, 4, 5]))

# 6th way using for loop with append and range
def remove_duplicate_6(list1):
    list2 = []
    for i in range(len(list1)):
        if list1[i] not in list2:
            list2.append(list1[i])
    return list2

print(remove_duplicate_6([1, 2, 3, 4, 5, 1, 2, 3, 4, 5]))

# 7th way using append and for loop
def remove_duplicate_7(list1):
    list2 = []
    for i in list1:
        if i not in list2:
            list2.append(i)
    return list2

print(remove_duplicate_7([1, 2, 3, 4, 5, 1, 2, 3, 4, 5]))

# 8th way using numpy
def remove_duplicate_8(list1):
    return np.unique(list1)

print(remove_duplicate_8([1, 2, 3, 4, 5, 1, 2, 3, 4, 5]))

