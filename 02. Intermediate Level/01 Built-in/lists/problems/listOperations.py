# Higher order function
# map() returns a map iterator object (which is an iterator)

def list_sum(list1):
    return list1 + list1

lst = [1, 2, 3, 4, 5]
sum = list(map(list_sum, lst))
print(sum)

sum = (map(lambda x: x + x, lst))
print(sum)

