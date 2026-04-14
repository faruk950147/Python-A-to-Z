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

'''
Step by Step 
lst = [1, 2, 3, 4, 5]
print(reduceFind(lst, add, 0))
start:
result = initial = 0
Iteration 1:
prev = 0
curr = 1
result = 0 + 1 = 1
Iteration 2:
prev = 1
curr = 2
result = 1 + 2 = 3
Iteration 3:
prev = 3
curr = 3
result = 3 + 3 = 6
Iteration 4:
prev = 6
curr = 4
result = 6 + 4 = 10
Iteration 5:
prev = 10
curr = 5
result = 10 + 5 = 15
Final Output:
15
সহজ ভাষায়

reduceFind() মানে:

"একটা result নিয়ে list-এর প্রতিটা element দিয়ে বারবার update করা"

Built-in reduce এর সাথে মিল

Python-এ already এটা আছে 

from functools import reduce

reduce(add, lst, 0)

তুমি basically নিজের হাতে এটা বানিয়েছো 

Bonus (Different Example)
Multiplication:
def mul(prev, curr):
    return prev * curr

print(reduceFind([1,2,3,4], mul, 1))

Output:

24
Pro Tip

তুমি চাইলে এটা আরও powerful করতে পারো 

result = callback(result, lst[i], i, lst)

তাহলে callback function এ:

index
পুরো list

দুটাই access করতে পারবে
'''
