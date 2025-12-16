def forFind(lst, callback):
    index = 0
    while index < len(lst):
        callback(lst[index])
        index += 1

def print_item(item):
    print(f"{item}")

numbers = [10, 20, 30, 40]
forFind(numbers, print_item)
