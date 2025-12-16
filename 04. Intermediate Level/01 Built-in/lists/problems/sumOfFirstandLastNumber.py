#. Sum of First and Last number in list


# 1. Using index
def sumOfFirstAndLastNumber(list):
    return list[0] + list[-1] # 1 + 5 = 6 it last index is found out
print(sumOfFirstAndLastNumber([1, 2, 3, 4, 5]))

# 2. Using len()
def sumOfFirstAndLastNumber(list):
    return list[0] + list[len(list) - 1] # 1 + 5 = 6 it last index is found out
print(sumOfFirstAndLastNumber([1, 2, 3, 4, 5]))

# 3. Using for loop
def sumOfFirstAndLastNumber(lst):
    first = None
    last = None
    
    for i in range(len(lst)):
        if i == 0:              # First element
            first = lst[i]
        if i == len(lst) - 1:   # Last element
            last = lst[i]
    
    return first + last
print(sumOfFirstAndLastNumber([1, 2, 3, 4, 5]))
