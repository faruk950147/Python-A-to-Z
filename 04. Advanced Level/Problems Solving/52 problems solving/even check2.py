T = int(input("Enter a number for test cases: "))  # first input: how many times to check

for _ in range(T):
    n = input("Enter a number: ").strip()  # input as string
    last_digit = int(n[-1])  # get last digit that means last index of string and convert to int
    
    if last_digit % 2 == 0:
        print("Even")  # if last digit is even
    else:
        print("Odd")   # if last digit is odd
                