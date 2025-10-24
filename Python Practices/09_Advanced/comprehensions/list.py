# def square_numbers(nums):
#     lst = []
#     for i in nums:
#         lst.append(i * i)
#     return lst

# nums = [1, 2, 3, 4, 5]
# print(square_numbers(nums))

# def sum_of(nums):
#     sum = 0
#     for i in range(1,nums+1):
#         sum += i
#     return sum 
 
# ========================== convert to list comprehension =========================
def square_numbers(nums):
    return [i * i for i in nums]

def sum_of(nums):
    return sum(i * i for i in range(1,nums+1))

nums = [1, 2, 3, 4, 5]
print(square_numbers(nums))
print(sum_of(nums))

def even_or_odd(nums):
    return [i for i in nums if i % 2 == 0]

def sum_of_evens(nums):
    return sum(i for i in nums if i % 2 == 0)

