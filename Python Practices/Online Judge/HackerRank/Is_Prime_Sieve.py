"""What does 6k mean?

6k means

a number that is a multiple of 6 —
in other words, it can be divided by 6 with no remainder.

Examples
k	6k	Calculation
0	0	6×0 = 0
1	6	6×1 = 6
2	12	6×2 = 12
3	18	6×3 = 18
4	24	6×4 = 24
5	30	6×5 = 30

So,
6k = 0, 6, 12, 18, 24, 30, 36, 42, 48 …

All are multiples of 6 

What does 6k ± 1 mean?

Now if you take those multiples of 6 and add or subtract 1,
you get numbers just one less or one more than a multiple of 6.

k	6k	6k - 1	6k + 1
1	6	5	7
2	12	11	13
3	18	17	19
4	24	23	25
5	30	29	31

Look —
many of these are prime numbers:
5, 7, 11, 13, 17, 19, 23, 29, 31 

Why is this important?

Every integer can be written as one of these six forms:

6
𝑘
,
 
6
𝑘
+
1
,
 
6
𝑘
+
2
,
 
6
𝑘
+
3
,
 
6
𝑘
+
4
,
 
6
𝑘
+
5
6k, 6k+1, 6k+2, 6k+3, 6k+4, 6k+5

But:

Numbers like 6k, 6k+2, 6k+3, 6k+4 are divisible by 2 or 3 

Only numbers of the form 6k−1 and 6k+1 are not divisible by 2 or 3 

So, for numbers greater than 3,
every prime number must be of the form 6k ± 1.

Summary

k → any integer

6k → multiples of 6

6k ± 1 → one less or one more than multiples of 6

Every prime number > 3 is of the form 6k−1 or 6k+1
"""
# def Is_Prime_Sieve(n):
#     if n <= 1:
#         return False
#     elif n <= 3:
#         return True
#     elif (n % 2) == 0 or (n % 3) == 0:
#         return False
#     else:
#         i = 5
#         while (i * i <= n):
#             if (n % i) == 0 or (n % (i + 2)) == 0:
#                 return False
#             i += 6
#     return True

# n = int(input())
# for x in range(1, n):
#     if Is_Prime_Sieve(x):
#         print(f'{x} is a prime number')
#     else:
#         print(f'{x} is not a prime number')
        
        
def Is_Prime_Sieve(n):
    if n <= 1: # 1 is not a prime number
        return False
    elif n <= 3: # 2 and 3 are prime numbers
        return True
    elif (n % 2) == 0 or (n % 3) == 0: # if n is divisible by 2 or 3, it's not a prime number
        return False
    else:
        for i in range(5, int(n ** 0.5) + 1, 6): # check for factors in the form of 6k ± 1
            if (n % i) == 0 or (n % (i + 2)) == 0: # if n is divisible by any of these, it's not a prime number
                return False
    return True

print(Is_Prime_Sieve(3))
