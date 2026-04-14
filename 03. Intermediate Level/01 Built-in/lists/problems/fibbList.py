def fibList(n):
    fibList = [1, 1]
    if n <= 2:
        return fibList[:n]
    fibPrev, fibCurr = 1, 1
    for i in range(3, n + 1):
        # swap and calculate next
        fibPrev, fibCurr = fibCurr, fibPrev + fibCurr
        fibList += [fibCurr]  # inefficient but works
    return fibList

print(fibList(10))

'''
def fibList(n):
    fibList = [1, 1]           # first two values
    if n <= 2:
        return fibList[:n]     # if input is 2 or less
    fibPrev, fibCurr = 1, 1    # previous and current values
    for i in range(3, n + 1):  # from 3 to n
        # swap and calculate next
        fibPrev, fibCurr = fibCurr, fibPrev + fibCurr
        fibList.append(fibCurr)   # add to list
    return fibList

print(fibList(10))

def fibList(n):
    fibList = [1, 1]
    if n <= 2:
        return fibList[:n]
    for i in range(2, n):
        # i starts from 2, so we can use fibList[-1] and fibList[-2]
        # fibList[-1] and fibList[-2] add
        fibList += [fibList[-1] + fibList[-2]]
    return fibList

print(fibList(10))


# Using append
def fibList(n):
    fibList = [1, 1]
    if n <= 2:
        return fibList[:n]
    for i in range(2, n):
        # fibList[-1] and fibList[-2] add
        fibList.append(fibList[-1] + fibList[-2])
    return fibList

print(fibList(10))

'''