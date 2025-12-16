def count_list(list1, item):
    print("list1 before counting: ", list1)
    return 'Item is counted', list1.count(item)

print(count_list([1, 2, 3, 4, 5], 3))