# Prime number
n = int(input("Enter a number: "))
if n < 2:
    print("Not a prime number")
else:
    for i in range(2, n):
        if n % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")

# leave your calculation
year = int(input("Enter a year: "))
if year % 4 == 0:
    print("Leap year")
else:
    print("Not a leap year")
    
year = int(input("Enter a year: "))
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")

year = int(input("Enter a year: "))
if year % 4 == 0:
    if year % 100 != 0 or year % 400 == 0:
        print("Leap year")
    else:
        print("Not a leap year")
else:
    print("Not a leap year")
    
# voting eligibility
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible for voting")
else:
    print("You are not eligible for voting")
