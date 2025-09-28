# def generate_coordinates(x, y, z, n):
#     # List comprehension 
#     result = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if (i + j + k) != n]
#     return result

# if __name__ == '__main__':
#     x = int(input())
#     y = int(input())
#     z = int(input())
#     n = int(input())

#     result = generate_coordinates(x, y, z, n)
    
    # print(result)
    
def generate_coordinates(x, y, z, n):
    result = []
    for i in range(x + 1):
        for j in range(y + 1):
            for k in range(z + 1):
                if i + j + k != n:
                    result.append([i, j, k])
    return result

if __name__ == '__main__':
    x = int(input("Enter the value of x: "))
    y = int(input("Enter the value of y: "))
    z = int(input("Enter the value of z: "))
    n = int(input("Enter the value of n: "))

    result = generate_coordinates(x, y, z, n)
    print(result)
