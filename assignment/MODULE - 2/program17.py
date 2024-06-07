# Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string. 

str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

if len(str1) < 2 or len(str2) < 2:
  print("Strings is too short.")
else:
  new_str1 = str2[:2] + str1[2:]
  new_str2 = str1[:2] + str2[2:]
  new_string = new_str1 + " " + new_str2
  print(f" string: {new_string}")