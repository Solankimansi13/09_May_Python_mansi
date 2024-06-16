# Write a Python program to calculate the area of a parallelogram 

def calculate_parallelogram_area(base, height):
    area = base * height
    return area

base = float(input("Enter the length of the base: "))
height = float(input("Enter the height of the parallelogram: "))

area = calculate_parallelogram_area(base, height)

print(f"The area of the parallelogram is {area} square units.")