'''
Write a Python function to calculate the factorial of a number (a 
nonnegative integer) 
'''

def calculate_factorial(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f

num = int(input("Enter a number: "))
print("Factorial of", num, "is", calculate_factorial(num))
