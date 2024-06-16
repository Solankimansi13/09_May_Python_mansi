#  Write a Python program to read a random line from a file. 

import random

with open('stdata.txt', 'r') as file:
    lines = file.readlines()
    random_line = random.choice(lines)

print(f"Random line from file: {random_line.strip()}")