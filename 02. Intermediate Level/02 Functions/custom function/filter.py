def filter(arr, callback):
    result = []
    for i in range(len(arr)):
        if callback(arr[i]):  # just value send
            result.append(arr[i])
    return result

print(filter([1, 2, 3, 4, 5], lambda value: value % 2 == 0))
