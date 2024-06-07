# Write a Python program to count occurrences of a substring in a string. 


string = input("Enter a String : ")
substring = input("Enter a Sub String : ")

total_count = string.count(substring)
print(f"the {substring} occurs {total_count} times.") 