def filter(arr, callback):
    result = []
    for i in range(len(arr)):
         # just value send to callback function that means is_even function is a predicate
        if callback(arr[i]): 
            result.append(arr[i])
    return result

def is_even(value):
    return value % 2 == 0

print(filter([1, 2, 3, 4, 5], is_even))