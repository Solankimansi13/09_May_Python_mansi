# Write a Python program to find the second smallest number in a list. 

n = input("Enter a list of numbers: ")
int_values = []

for i in n:
    if i.isdigit():
        int_values.append(int(i))

num1, num2 = None, None
for i in int_values:
    if num1 is None or i < num1:
        num1, num2 = i, num1
    elif num2 is None or i < num2:
        num2 = i

print(num2)