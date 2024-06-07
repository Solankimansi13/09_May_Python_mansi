# Write a python program to sum of the first n positive integers. 

number = int(input("how many number's sum you want to print :- "))

i = 1
sum = 0
 
for i in range(number+1):
    sum = sum + i
    i = i + 1

print(f"The sum of total is {sum}")