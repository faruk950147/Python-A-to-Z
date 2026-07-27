def sumOfNNum(nums, elements):
    """
    Calculate the sum of n numbers.
    
    Args:
        nums (int): Number of elements.
        elements (list): List of elements.
        
    Returns:
        int: Sum of the elements.
    """
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

