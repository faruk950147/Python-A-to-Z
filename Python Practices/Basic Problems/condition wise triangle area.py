import math
def triangleArea(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        s = (a + b + c) / 2
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5
    else:
        return "Invalid triangle"
    
print(triangleArea(3, 4, 5))

def triangleArea(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))
    else:
        return "Invalid triangle"
    
print(triangleArea(3, 4, 5))
