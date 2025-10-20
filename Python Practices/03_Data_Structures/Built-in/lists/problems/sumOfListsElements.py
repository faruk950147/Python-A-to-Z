def sumOfList(list1):
    return sum(list1)
print(sumOfList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

def sumOfListsElements(list1):
    sum = 0
    for i in range(len(list1)):
        sum += list1[i]
    return sum

print(sumOfListsElements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
