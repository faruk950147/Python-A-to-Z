"""
circle is a round shape
 pi = 3.14 is a constant value
 radius is the distance from the center to the edge
 diameter is the distance across the circle
 circumference is the distance around the circle
 area is the space inside the circle
"""

def circle_area(radius):
    """
    Calculate the area of a circle given its radius.
    
    Formula: A = π * r²
    Where π ≈ 3.14159
    """
    return 3.14 * radius * radius

print(circle_area(5))


def circle_circumference(radius):
    """
    Calculate the circumference of a circle given its radius.
    
    Formula: C = 2 * π * r
    Where π ≈ 3.14159
    """
    return 2 * 3.14 * radius

print(circle_circumference(5))


def circle_diameter(radius):
    """
    Calculate the diameter of a circle given its radius.
    
    Formula: d = 2 * r
    """
    return 2 * radius

print(circle_diameter(5))

def circle_radius(radius):
    """
    Calculate the radius of a circle given its radius.
    
    Formula: r = r
    """
    return radius

print(circle_radius(5))

def circle_height(radius):
    """
    Calculate the height of a circle given its radius.
    
    Formula: h = r
    """
    return radius

print(circle_height(5))

def circle_volume(radius):
    """
    Calculate the volume of a circle given its radius.
    
    Formula: V = 4/3 * π * r³
    Where π ≈ 3.14159
    """
    return 4/3 * 3.14 * radius * radius * radius

print(circle_volume(5)) 

def circle_surface_area(radius):
    """
    Calculate the surface area of a circle given its radius.
    
    Formula: SA = 4 * π * r²
    Where π ≈ 3.14159
    """
    return 4 * 3.14 * radius * radius

print(circle_surface_area(5))

def circle_surface_volume(radius):
    """
    Calculate the surface volume of a circle given its radius.
    
    Formula: SV = 4/3 * π * r³
    Where π ≈ 3.14159
    """
    return 4/3 * 3.14 * radius * radius * radius

print(circle_surface_volume(5))

def circleOfPerimeter(radius):
    """
    Calculate the perimeter of a circle given its radius.
    
    Formula: P = 2 * π * r
    Where π ≈ 3.14159
    """
    return 2 * 3.14 * radius

print(circleOfPerimeter(5))