def max_min(lst):
    return max(lst), min(lst)

print(max_min([1, 2, 3, 4, 5]))

def max_min_2(lst):
    max = lst[0]
    min = lst[0]
    for i in lst:
        if i > max:
            max = i
        if i < min:
            min = i
    return max, min

print(max_min_2([1, 2, 3, 4, 5]))

def max_min_3(lst):
    max = lst[0]
    min = lst[0]
    for i in range(1, len(lst)):
        if lst[i] > max:
            max = lst[i]
        if lst[i] < min:
            min = lst[i]
    return max, min

print(max_min_3([1, 2, 3, 4, 5]))
