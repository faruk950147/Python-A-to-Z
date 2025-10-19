def foreachFind(lst, callback):
    for i in range(len(lst)):
        callback(lst[i])


def print_item(item):
    print(f"{item}")

numbers = [1, 2, 3, 4, 5]
foreachFind(numbers, print_item)