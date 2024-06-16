# Write a Python program to calculate surface volume and area of a cylinderimport math
import math

def calculate_cylinder_properties(radius, height):
    volume = math.pi * radius ** 2 * height
    surface_area = 2 * math.pi * radius * (radius + height)
    return volume, surface_area

radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))

volume, surface_area = calculate_cylinder_properties(radius, height)

print(f"The volume of the cylinder is {volume:.2f} cubic units.")
print(f"The surface area of the cylinder is {surface_area:.2f} square units.")