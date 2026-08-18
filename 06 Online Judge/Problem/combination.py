import math
def combination(s):
    if len(s) == 0:
        return []
    if len(s) == 1:
        return [s]

    result = []
    # first character fix
    for i in range(len(s)):
        char = s[i]
        remaining = s[:i] + s[i+1:]

        # combination of remaining string
        for c in combination(remaining):
            result.append(char + c)
    return result


def nCr(n, r):
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

print(nCr(5, 2))  # Output: 10

