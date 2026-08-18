import math


class Combination:

    def permutation(self, s):
        if len(s) == 0:
            return []

        if len(s) == 1:
            return [s]

        result = []

        # first character fix
        for i in range(len(s)):
            char = s[i]
            remaining = s[:i] + s[i + 1:]

            # permutation of remaining string
            for c in self.permutation(remaining):
                result.append(char + c)

        return result


    def nCr(self, n, r):
        return math.factorial(n) // (
            math.factorial(r) * math.factorial(n - r)
        )


combination = Combination()

print(combination.permutation("ABC"))

print(combination.nCr(5, 2))

