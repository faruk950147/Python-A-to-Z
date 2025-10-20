def remove_item(list1, item):
    list1.remove(item)
    return list1

print(remove_item([1, 2, 3, 4, 5], 3))

def pop_2list(list1, index):
    list1.pop(index)
    return list1

print(pop_2list([1, 2, 3, 4, 5], 3))

def clear_2list(list1):
    print("list1 before clearing: ", list1)
    list1.clear()
    return 'List1 is cleared', list1
print(clear_2list([1, 2, 3, 4, 5]))

def del_2list(list1):
    print("list1 before deletion: ", list1)
    del list1
    return 'List1 is deleted'

print(del_2list([1, 2, 3, 4, 5]))


def del_item(list1, index):
    print("list1 before deletion: ", list1)
    del list1[index]
    return 'Item is deleted', list1

print(del_item([1, 2, 3, 4, 5], 3))
