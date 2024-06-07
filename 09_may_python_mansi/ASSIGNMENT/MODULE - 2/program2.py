# Write a Python program to get the Factorial number of given number. /
# factorial number is multiplication of given number. 
# for ex:- factorial of 5 is = 1*2*3*4*5=120

number = int(input("Enter the number = "))

factorial = 1

a = 1

while a <= number:
    factorial = factorial * a
    a = a+1
print(f"Factorial of {number} is {factorial}")


# /using for loop


number = int(input("Enter a number: "))
factorial = 1
for i in range(1, number+1):
    factorial = factorial * i      
print(f"Factorial of {number} is {factorial}")