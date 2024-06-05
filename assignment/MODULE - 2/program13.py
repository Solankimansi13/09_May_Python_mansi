# Write a Python program to count the number of characters (character frequency) in a string

string = input("Enter a string: ")
char_frequency = {}  # Initialize an empty dictionary

for char in string:
  if char in char_frequency:
    char_frequency[char] += 1  # Increment the count if the character exists
  else:
    char_frequency[char] = 1  # Initialize the count to 1 if the character is new

print("Character frequencies:")
for char, count in char_frequency.items():
  print(f"'{char}': {count}")