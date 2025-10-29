import random

min_value = 1
max_value = 6

roll_again = ""

while roll_again.lower() != "n":
    print("Rolling the dice...")
    print("The value is", random.randint(min_value, max_value))
    roll_again = input("Do you want to roll again? (y/n): ")
