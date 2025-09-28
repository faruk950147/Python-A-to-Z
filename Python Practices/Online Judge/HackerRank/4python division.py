def perform_division(a, b):
    print(a // b)  # Integer division 
    print(a / b)   # Float division 

if __name__ == '__main__':
    a = int(input())  # first number input
    b = int(input())  # second number input
    perform_division(a, b)  