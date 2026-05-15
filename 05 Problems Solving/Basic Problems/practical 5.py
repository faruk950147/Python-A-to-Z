import math
import itertools

n = 5 # total number of items
r = 2 # number of items to choose

result = math.comb(n, r)
print(result)   # Output: 10

def nCr(n, r):
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

print(nCr(5, 2))  # Output: 10


n = [1, 2, 3, 4, 5] # total number of items
r = 2 # number of items to choose

combinations = list(itertools.combinations(n, r))
print(combinations)   # [(1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 4), (3, 5), (4, 5)]
print("Total:", len(combinations))   # 10



def nCr(n, r):
    if r > n:
        return 0   
    return math.comb(n, r) 

n = int(input("Enter n: ")) # total number of items
r = int(input("Enter r: ")) # number of items to choose

print(f"{n}C{r} = {nCr(n, r)}")


def nPr(n, r):
    if r > n:
        return 0   
    return math.perm(n, r) 

n = int(input("Enter n: ")) # total number of items
r = int(input("Enter r: ")) # number of items to choose

print(f"{n}P{r} = {nPr(n, r)}")


def nPr(n, r):
    if r > n:
        return 0
    return math.factorial(n) // math.factorial(n - r)

print(nPr(5, 2))  # Output: 20
