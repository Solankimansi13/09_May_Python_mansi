# Write a Python program to count occurrences of a substring in a string. 

string = input("Enter the main string: ")
substring = input("Enter the substring to count: ")

count = 0
start_index = 0

while True:
  start_index = string.find(substring, start_index)
  if start_index == -1:
    break
  count += 1
  start_index += len(substring)  # Move to the next possible position

print(f"The substring '{substring}' appears {count} times in the string '{string}'.")