# # Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return 
# instead of the empty string. 

def first_and_last_char(text):
    if len(text) < 2:
        return ""
    else:
        return text[:2] + text[-2:]


strings = int(input("Enter the number of strings: "))

for i in range(strings):
    string = input(f"Enter string {i+1}: ")
    print(f"String '{string}': {first_and_last_char(string)}")
