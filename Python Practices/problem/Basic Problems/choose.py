import random

numbers = list(range(1, 11))   
choosen = []

while len(choosen) < 5:
    number = random.choice(numbers)
    numbers.remove(number)
    choosen.append(number)

choosen.sort()
print("Choosen:", choosen)

print("Sample from remaining:", random.sample(numbers, 3))


choosen = []
while len(choosen) < 5:
    number = random.choice(numbers)
    if number not in choosen:
        choosen.append(number)
print(choosen)





