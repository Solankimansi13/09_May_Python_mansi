# Write a Python program to check if a number is positive, negative or zero.

number = int(input("ENTER THE NUMBER = "))

if number < 0:
    print("number is negative.")
elif number > 0:
    print("number is positive.")
elif number == 0:
    print("zero.")
else:
    print("please enter valid input.")