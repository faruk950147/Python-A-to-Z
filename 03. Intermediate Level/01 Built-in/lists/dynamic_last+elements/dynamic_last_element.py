def dynamic_last_element(fruits):
    if len(fruits) > 0:
        # fruits[index] thats mean list of index?
        # fruits → list
        # [index] → list index we want which item
        # len(fruits) - 1 → last index
        # fruits[len(fruits) - 1] → last item
        # return fruits[len(fruits) - 1] → return last item
        # why fruits[len(fruits) - 1]? this inside of dynamic
        return fruits[len(fruits) - 1]
    return None


print(dynamic_last_element(["apple", "banana", "cherry", "Orange", "Mango", "Grape"]))
