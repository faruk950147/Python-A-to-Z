import math
def permutation(s):
    if len(s) == 0:
        return []
    if len(s) == 1:
        return [s]

    result = []
    # first character fix
    for i in range(len(s)):
        char = s[i]
        remaining = s[:i] + s[i+1:]

        # permutation of remaining string
        for p in permutation(remaining):
            result.append(char + p)
    return result


print(permutation("abc"))


def nPr(n, r):
    if r > n:
        return 0   
    return math.perm(n, r) 

print(nPr(5, 2))


def nPr(n, r):
    if r > n:
        return 0
    return math.factorial(n) // math.factorial(n - r)  # noqa: F821

print(nPr(5, 2))  # Output: 20
