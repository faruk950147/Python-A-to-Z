# sum of n series
from turtle import circle


n = int(input("Enter a number: "))
if n < 0:
    print("Enter a positive number")
else:
    sum = 0
    for i in range(1, n + 1):
        sum += i
    print("The sum of", n, "series is", sum)
    
    
# sum of n series
n = int(input("Enter a number: "))
if n < 0:
    print("Enter a positive number")
else:
    sum = 0
    while n > 0:
        sum += n
        n -= 1
    print("The sum of", n, "series is", sum)



# sum of n series and average
n = int(input("Enter a number: "))
if n < 0:
    print("Enter a positive number")
else:
    sum = 0
    while n > 0:
        sum += n
        n -= 1
    print("The sum of", n, "series is", sum)
    print("The average of", n, "series is", sum / n)
    
    
# kilometer to meter
kilometer = float(input("Enter a distance in kilometers: "))
meter = kilometer * 1000
print(kilometer, "kilometers is equal to", meter, "meters")


# meter to kilometer
meter = float(input("Enter a distance in meters: "))
kilometer = meter / 1000
print(meter, "meters is equal to", kilometer, "kilometers")


# kilometer to miles
kilometer = float(input("Enter a distance in kilometers: "))
miles = kilometer * 0.621371
print(kilometer, "kilometers is equal to", miles, "miles")


# miles to kilometer
miles = float(input("Enter a distance in miles: "))
kilometer = miles / 0.621371
print(miles, "miles is equal to", kilometer, "kilometers")

# area of circle calculate
radius = float(input("Enter the radius of the circle: "))
area = 3.14 * radius * radius
print("The area of the circle is", area)

# square of area of circle
def square_of_arm(arm):
    return arm * arm

print("The square of the area of the circle is", square_of_arm(area))

# rombus area calculate rectangle calculate
d1 = float(input("Enter the first diagonal of the rombus: "))
d2 = float(input("Enter the second diagonal of the rombus: "))
area = 0.5 * d1 * d2
print("The area of the rombus is", area)

# sphere area calculate and volume calculate and rectangle calculate and square calculate
radius = float(input("Enter the radius of the sphere: "))
sphere_area = 4 * 3.14 * radius * radius
sphere_volume = 4/3 * 3.14 * radius * radius * radius
print("The area of the sphere is", sphere_area)
print("The volume of the sphere is", sphere_volume)

# rectangle area calculate and perimeter calculate
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
rectangle_area = length * width
rectangle_perimeter = 2 * (length + width)
print("The area of the rectangle is", rectangle_area)
print("The perimeter of the rectangle is", rectangle_perimeter)
