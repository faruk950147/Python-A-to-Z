def reduceFind(lst, callback, initial):
    # list iteration work in all elements
    # callback function work in updated result and current element
    # callback function return updated result
    # initial is the first value of result
    result = initial
    for i in range(len(lst)):
        # just value send if we want to send index and list then use lst[i], i, lst
        # result = callback(result, lst[i], i, lst)
        result = callback(result, lst[i]) 
    return result

# just a callback
def add(prev, curr): # just value send if we want to send index and list then use lst[i], i, lst
    # previous is the updated result
    # current is the current element
    # return updated result
    # prev + curr
    return prev + curr 

lst = [1, 2, 3, 4, 5]
print(reduceFind(lst, add, 0))
