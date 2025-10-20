def copy_list(list1):
    print("list1 before copying: ", list1)
    return 'List1 is copied', list1.copy()

print(copy_list([1, 2, 3, 4, 5]))