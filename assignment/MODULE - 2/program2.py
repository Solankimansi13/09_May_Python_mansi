#Write a Python program to get the Factorial number of given number.




num = int(input("Enter a number: "))
factorial = 1
if num < 0:
  print(" please enter a positive number. ")
elif num == 0:
  print("The factorial of 0 is 1")
else:
  for i in range(1, num + 1):
    factorial *= i
  print(f"The factorial of{num} is {factorial}")