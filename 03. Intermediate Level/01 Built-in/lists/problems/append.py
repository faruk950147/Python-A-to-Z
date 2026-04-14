
def append_item(list1, item):
    list1.append(item)
    return list1

print(append_item([1, 2, 3], 4))

def append_2list(list1, list2):
    list1.append(list2)
    return list1

print(append_2list([1, 2, 3], [4, 5, 6]))



def append_item(list1=None, item=None):
    if list1 is None:
        list1 = []
    list1.append(item)
    return list1

print(append_item([1, 2, 3], 4))

def append_2list(list1=None, list2=None):
    if list1 is None:
        list1 = []
    if list2 is None:
        list2 = []
    list1.append(list2)
    return list1

print(append_2list([1, 2, 3], [4, 5, 6]))