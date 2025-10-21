list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
for i in range(len(list1)):
    sum1 = 0
    for j in range(len(list2)):
        sum1 += list1[i] + list2[j]
    print(sum1)