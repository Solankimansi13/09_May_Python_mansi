# Write a Python function to check whether a number is in a given range 


def range(num, start, end):
    if num >= start and num <= end:
        return True
    else:
        return False

num = int(input("Enter a number: "))
start = int(input("Enter start of the range: "))
end = int(input("Enter end of the range: "))

if range(num, start, end):
    print(f"{num} is in the range [{start}, {end}]")
else:
    print(f"{num} is not in the range [{start}, {end}]")