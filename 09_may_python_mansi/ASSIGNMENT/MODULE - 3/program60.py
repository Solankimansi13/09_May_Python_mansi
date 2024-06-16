# Write a Python program to convert degree to radian 


import math

def convert_to_radians(degrees):
    radians = math.radians(degrees)
    return radians

degrees = float(input("Enter degrees: "))
radians = convert_to_radians(degrees)

print(f"{degrees} degrees is equal to {radians} radians")