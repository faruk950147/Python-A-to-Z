#. Sum of First and Last character in string

# 1. Using index
def sumOfFirstAndLastCharacter(string):
    return string[0] + string[-1]
print(sumOfFirstAndLastCharacter("Hello"))

# 2. Using len()
def sumOfFirstAndLastCharacter(string):
    return string[0] + string[len(string) - 1]
print(sumOfFirstAndLastCharacter("Hello"))

# 3. Using for loop
def sumOfFirstAndLastCharacter(string):
    first = None
    last = None
    
    for i in range(len(string)):
        if i == 0:              # First character
            first = string[i]
        if i == len(string) - 1:   # Last character
            last = string[i]
    
    return first + last
print(sumOfFirstAndLastCharacter("Hello"))
