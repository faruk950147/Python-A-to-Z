import random

numbers = list(range(1, 11))  

choosen = []
winers = 3
while len(choosen) < winers:
    number = random.choice(numbers)
    if number not in choosen:
        choosen.append(number)
print(choosen)

''' 
# Method 1: Using random.choice with list removal
choosen = []
while len(choosen) < 5:
    number = random.choice(numbers)
    if number not in choosen:
        choosen.append(number)
print(choosen)

# Method 2: Using random.choice with list removal
choosen = []
while len(choosen) < 5:
    number = random.choice(numbers)
    numbers.remove(number)
    choosen.append(number)

choosen.sort()
print("Choosen:", choosen)

print("Sample from remaining:", random.sample(numbers, 3))

'''




