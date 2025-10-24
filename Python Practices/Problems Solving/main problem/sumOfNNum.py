# nums = int(input("How many numbers you want to operations: "))
# sum = 0
# for i in range(nums):
#     num = int(input("Enter a number: "))
#     sum += num
# print("The sum of the numbers is: ", sum)

def sumOfNNum(nums, elements):
    sum = 0
    for i in range(nums):
        sum += elements[i]
    return sum

nums = int(input("How many numbers you want to operations: "))
elements = []
for i in range(nums):
    element = int(input("Enter a number: "))
    elements.append(element)
print(sumOfNNum(nums, elements))

