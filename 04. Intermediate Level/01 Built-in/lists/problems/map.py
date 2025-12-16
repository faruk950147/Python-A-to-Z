# map() takes two parameters:
# 1. function
# 2. iterable

# def square(num):
#     return num ** 2

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# squared = map(square, nums)
# print(list(squared))


def find_length(word):
    return len(word)

words = ['apple', 'banana', 'cherry', 'date']
lengths = map(find_length, words)
print(list(lengths))

