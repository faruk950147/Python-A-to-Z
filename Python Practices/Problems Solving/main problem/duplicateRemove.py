def removeDuplicates(lst):
    return list(set(lst))

print(removeDuplicates([1, 2, 2, 3, 3, 4, 5, 5, 6, 6]))

# output: [1, 2, 3, 4, 5, 6]

def removeDuplicates1(lst):
    return list(dict.fromkeys(lst))

print(removeDuplicates1([1, 2, 2, 3, 3, 4, 5, 5, 6, 6]))

# output: [1, 2, 3, 4, 5, 6]

def removeDuplicates2(lst):
    result = []
    for i in lst:
        if i not in result:
            result.append(i)
    return result

print(removeDuplicates2([1, 2, 2, 3, 3, 4, 5, 5, 6, 6]))

# output: [1, 2, 3, 4, 5, 6]
def removeDuplicates3(lst):
    result = []
    for i in lst:
        if lst.count(i) >= 1 and i not in result:
            result.append(i)
    return result

print(removeDuplicates([1, 2, 2, 3, 3, 4, 5, 5, 6, 6]))

# output: [1, 2, 3, 4, 5, 6]
