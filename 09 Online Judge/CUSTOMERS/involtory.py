# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    # input 
    x = int(input())
    shoe_sizes = list(map(int, input().split()))
    n = int(input())

    # shoe_sizes of stock in dictionary 
    stock = {}

    # shoe_sizes of stock loop
    for size in shoe_sizes:
        if size in stock:
            stock[size] += 1
        else:
            stock[size] = 1

    earnings = 0

    # n number of customers loop
    for _ in range(n):
        size, price = map(int, input().split())
        if size in stock and stock[size] > 0:
            earnings += price
            stock[size] -= 1

    # output the total earnings
    print(earnings)

def calculate_earnings(x, shoe_sizes, customers):
    # shoe_sizes of stock in dictionary
    # shoe_sizes of stock loop
    stock = {}
    for size in shoe_sizes:
        if size in stock:
            stock[size] += 1
        else:
            stock[size] = 1

    earnings = 0

    # n number of customers loop
    # n number of customers loop
    for size, price in customers:
        if size in stock and stock[size] > 0:
            earnings += price
            stock[size] -= 1

    return earnings


if __name__ == '__main__':
    x = int(input())
    shoe_sizes = list(map(int, input().split()))
    n = int(input())
    customers = [tuple(map(int, input().split())) for _ in range(n)]

    total_earnings = calculate_earnings(x, shoe_sizes, customers)
    print(total_earnings)
    
    
from collections import Counter
def calculate_earnings(shoe_sizes, customers):
    stock = Counter(shoe_sizes)
    earnings = 0

    for size, price in customers:
        if stock[size]:
            earnings += price
            stock[size] -= 1

    return earnings


if __name__ == '__main__':
    x = int(input())
    shoe_sizes = list(map(int, input().split()))
    n = int(input())
    customers = [tuple(map(int, input().split())) for _ in range(n)]

    total_earnings = calculate_earnings(shoe_sizes, customers)
    print(total_earnings)
