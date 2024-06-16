# Write a Python program to find the maximum and minimum numbers from the specified decimal numbers.

def find_max_min(numbers):
    max_num = max(numbers)
    min_num = min(numbers)
    return max_num, min_num

numbers = input("Enter decimal numbers (separated by space): ")
numbers = list(map(float, numbers.split()))

max_num, min_num = find_max_min(numbers)

print(f"Maximum number: {max_num}")
print(f"Minimum number: {min_num}")
