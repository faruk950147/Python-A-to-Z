"""
def print_squares(n):
    for i in range(n):  # 0 to n-1
        print(i*i)  # print square of i

if __name__ == '__main__':
    n = int(input())  # read integer from input
    print_squares(n)  # call function with n
    
    
def print_squares(n):
    if n < 0:
        print("Negative number")
    else:
        for i in range(n):
            print(i*i)

if __name__ == '__main__':
    n = int(input(""))
    print_squares(n)
    
    def print_squares(n):
    if n < 0:
        print("Negative number")
    else:
        for i in range(n):
            print(i**2)

if __name__ == '__main__':
    n = int(input(""))
    print_squares(n)


    
"""


def print_consecutive_numbers(n):
    for i in range(1, n+1):
        print(i, end='')

if __name__ == '__main__':
    n = int(input())
    print_consecutive_numbers(n)



if __name__ == '__main__':
    n = int(input())
    for i in range(1, n+1):
        print(i, end='')