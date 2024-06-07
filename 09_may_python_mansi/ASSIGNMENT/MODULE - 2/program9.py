#  Write a Python program to sum of three given integers. However, if two values are equal sum will be zero. 

a = int(input("Enter a number one :- "))
b = int(input("Enter a number two :- "))
c =int(input("Enter a number three :- "))
 
if a == b  or b == c or c == a:
    print("Sum is Zero , because two values are equal.")
else:
    print("the sum of three number is ", a+b+c)