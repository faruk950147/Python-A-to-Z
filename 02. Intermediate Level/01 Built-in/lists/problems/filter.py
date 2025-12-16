# filter() takes two parameters:
# 1. function
# 2. iterable

def is_even(num):
    return num % 2 == 0

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = filter(is_even, nums)
print(list(evens))

# or

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = filter(lambda num: num % 2 == 0, nums)
print(list(evens))


laptops = {"hp": 500000, "dell": 600000, "apple": 1000000, "lenovo": 400000, "asus": 300000}
budget = int(input("Enter your budget: "))
def is_find(element):
    if laptops[element] >= budget:
        return True
    return False
apple_laptops = filter(is_find, laptops)
print(list(apple_laptops))


