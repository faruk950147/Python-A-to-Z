def index_list(list1, item):
    print("list1 before indexing: ", list1)
    return 'Item is indexed', list1.index(item)

print(index_list([1, 2, 3, 4, 5], 3))