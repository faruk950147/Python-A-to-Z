def sumOfElement(lst):
    if isinstance(lst, list):
        total = 0
        for item in range(len(lst)):
            if isinstance(lst[item], (int, float)):  # just int or float will be added
                total += lst[item]
            # non-number ignore 
        return total
    else:
        return "Please provide a list"

# Test
print(sumOfElement([1, 2, 3, 4, 5, "a"]))  # Output: 15
print(sumOfElement([1, 2.5, "hello", {"a":1}, (1,2), {1,2,3}, 3]))  # Output: 6.5


def sumOfElement2(lst):
    if isinstance(lst, list):
        total = 0
        for item in lst:
            if isinstance(item, (int, float)):  # just int or float will be added
                total += item
            # non-number ignore 
        return total
    else:
        return "Please provide a list"

# Test
print(sumOfElement2([1, 2, 3, 4, 5, "a"]))  # Output: 15
print(sumOfElement2([1, 2.5, "hello", {"a":1}, (1,2), {1,2,3}, 3]))  # Output: 6.5