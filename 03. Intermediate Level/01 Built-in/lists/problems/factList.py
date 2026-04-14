# Using +=
def factList(n):
    factList = [1, 1]           # first two values
    if n <= 2:
        return factList[:n]     # if input is 2 or less
    fact = 2                    # 2! = 2
    for i in range(3, n + 1):   # from 3 to n
        fact *= i               # previous value * i
        factList += [fact]      # add to list
    return factList

print(factList(10))

'''

# Using append
def factList(n):
    factList = [1, 1]           # first two values
    if n <= 2:
        return factList[:n]     # if input is 2 or less
    fact = 2                    # 2! = 2
    for i in range(3, n + 1):   # from 3 to n
        fact *= i               # previous value * i
        factList.append(fact)   # add to list
    return factList

print(factList(10))

def factList(n):
    factList = [1]
    if n == 0:
        return factList[:1]
    for i in range(1, n):
        factList += [factList[-1] * (i + 1)]
    return factList

print(factList(10))

def factList(n):
    factList = [1]  # 0! = 1
    if n == 0:
        return factList[:1]
    for i in range(1, n):  # from 1 to n
        factList.append(factList[-1] * (i + 1))  # last value * (i+1)
    return factList

print(factList(10))

'''
