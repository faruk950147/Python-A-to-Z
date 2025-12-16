def givenListEvenOdd(list1):
    even = []
    odd = []
    for i in range(len(list1)):
        if list1[i] % 2 == 0:
            even += [list1[i]]
        else:
            odd += [list1[i]]
    return even, odd

print(givenListEvenOdd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# 2nd way using list append

def givenListEvenOdd(list1):
    even = []
    odd = []
    for i in range(len(list1)):
        if list1[i] % 2 == 0:
            even.append(list1[i])
        else:
            odd.append(list1[i])
    return even, odd

print(givenListEvenOdd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

