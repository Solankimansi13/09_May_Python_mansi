#  Write python program that swap two number with temp variable and without temp variable.

print("---------------------------Swapping with a temp variable----------------------")

num1 =int(input("enter the number 1 = "))
num2 =int(input("enter the number 2 = "))

temp = num1
print(f"the value of temp is {temp} ")
num1 = num2
print(f"the value of number 1 is now {num1}")
num2 = temp
print(f"the value of number 2 is now {num2}")



print("----------------------------Swapping without a temporary variable-----------------")

num1 = int(input("enter the number 1 = "))
num2 = int(input("enter the number 2 = "))

num1,num2 = num2,num1

print("after swapping")
print("the value of num1 is ",num1)
print("the value of num2 is ",num2)