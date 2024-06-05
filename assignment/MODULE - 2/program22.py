# # Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return 
# instead of the empty string. 

def first_and_last_chars(text):
  if len(text) < 2:
    return ""
  else:
    return text[:2] + text[-2:]

# Example usage:
string1 = "mansiii"
string2 = "python"
string3 = "hello world"

print(f"String '{string1}': {first_and_last_chars(string1)}")
print(f"String '{string2}': {first_and_last_chars(string2)}")
print(f"String '{string3}': {first_and_last_chars(string3)}")