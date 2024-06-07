#  Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.


number1 = int(input("Enter number one :- "))
number2  = int(input("Enterr number two :- "))
 
if number1 == number2 or number2 + number1 == 5 or number1 - number2 == 5:
    print("True.")
else:
    print("Flase.")