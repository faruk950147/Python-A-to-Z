def max_min(lst):
    return max(lst), min(lst)

print(max_min([1, 2, 3, 4, 5]))

def max_min_2(lst):
    max = lst[0]
    min = lst[0]
    for item in lst:
        if item > max:
            max = item
        if item < min:
            min = item
    return max, min

print(max_min_2([1, 2, 3, 4, 5]))

def max_min_3(lst):
    max = lst[0]
    min = lst[0]
    for item in range(1, len(lst)):
        if lst[item] > max:
            max = lst[item]
        if lst[item] < min:
            min = lst[item]
    return max, min

print(max_min_3([1, 2, 3, 4, 5]))
