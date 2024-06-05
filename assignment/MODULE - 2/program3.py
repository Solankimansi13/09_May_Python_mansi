#Write a Python program to get the Fibonacci series of given range.
'''
f0 =0
f1= f0+ 1
f2= f0 +f1
f3 = f2+f1
f4= f3 + f2 
'''
#fibbonaci sequence

# number = int(input("Enter the number of terms: "))

# n1, n2 = 0, 1
# count = 0

# if number <= 0:
#   print("enter a positive number")
# elif number == 1:
#   print(f"Fibonacci sequence {number} :")
#   print(n1)
# else:
#   print(f"Fibonacci sequence {number} :")
#   while count < number:
#     print(n1, end=" ")
#     nth = n1 + n2
#     n1 = n2
#     n2 = nth
#     count += 1



number = int(input("how many number you want to print : "))

n1 , n2 = 0, 1
count = 0
total_sum = 0  

if number <= 0:
  print("Please enter a positive number.")
elif number == 1:
  print("Fibonacci sequence ", number, ":")
  print(n1)
else:
  print("Fibonacci sequence ", number, ":")
  while count < number:
    print(n1, end=" ")
    total_sum += n1  
    nth = n1 + n2
    n1 = n2
    n2 = nth
    count += 1

print("\nSum of the Fibonacci series:", total_sum)