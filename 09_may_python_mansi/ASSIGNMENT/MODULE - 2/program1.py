# # Write a Python program to check if a number is positive, negative or zero.

number = float(input("Enter a number = "))

if number > 0:
    print("The number is positive.")

elif number < 0:
    print("The number is negative.")

elif number == 0:
    print("zero.")

else:
    print("please enter a valid input.")



'''


Method 2: Using if-else with nested conditions

num = float(input("Enter a number: "))
if num > 0:
 print("The number is positive")

 else:
 if num < 0:
 print("The number is negative")
 else:
 print("The number is zero")
---------------------------------------------------------------------------------------

Method 3: Using a ternary operator

num = float(input("Enter a number: "))
print("The number is " + ("positive" if num > 0 else "negative" if num < 0 else "zero"))


 '''
