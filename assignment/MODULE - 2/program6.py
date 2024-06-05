#  Write python program that swap two number with temp variable and without temp variable.



print("Swapping with a temp variable")

num1 =int(input("enter the number 1 = "))
num2 =int(input("enter the number 2 = "))


temp = num1
num1 = num2
num2 = temp

print(f"After Swapping: num1 = {num1} and num2 = {num2}")

print("Swapping without a temporary variable")

num1 = int(input("enter the number 1 = "))
num2 = int(input("enter the number 2 = "))

num1 = num1 + num2  
num2 = num1 - num2  
num1 = num1 - num2  

print(f"After Swapping: num1 = {num1} and num2 = {num2}")