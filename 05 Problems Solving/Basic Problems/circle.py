"""
circle is a round shape
 pi = 3.14 is a constant value
 radius is the distance from the center to the edge
 diameter is the distance across the circle
 circumference is the distance around the circle
 area is the space inside the circle
"""

def circle_area(radius):
    return 3.14 * radius * radius

print(circle_area(5))


def circle_circumference(radius):
    return 2 * 3.14 * radius

print(circle_circumference(5))


def circle_diameter(radius):
    return 2 * radius

print(circle_diameter(5))

def circle_radius(radius):
    return radius

print(circle_radius(5))

def circle_height(radius):
    return radius

print(circle_height(5))

def circle_volume(radius):
    return 4/3 * 3.14 * radius * radius * radius

print(circle_volume(5)) 

def circle_surface_area(radius):
    return 4 * 3.14 * radius * radius

print(circle_surface_area(5))

def circle_surface_volume(radius):
    return 4/3 * 3.14 * radius * radius * radius

print(circle_surface_volume(5))

def circleOfPerimeter(radius):
    return 2 * 3.14 * radius

print(circleOfPerimeter(5))