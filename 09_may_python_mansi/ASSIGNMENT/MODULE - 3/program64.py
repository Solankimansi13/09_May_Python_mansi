# Write a Python program to returns sum of all divisors of a number 

def sum_of_divisors(n):
    sum = 0
    for i in range(1, n + 1):
        if n % i == 0:
            sum += i
    return sum

num = int(input("Enter a number: "))
result = sum_of_divisors(num)

print(f"The sum of divisors of {num} is {result}")