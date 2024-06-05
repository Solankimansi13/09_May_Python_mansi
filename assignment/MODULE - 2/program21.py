#  Write a Python function to reverses a string if its length is a multiple of 4. 

def reverse_if_multiple_of_4(text):
 
  if len(text) % 4 == 0:
    return text[::-1]
  else:
    return text

# Example usage:
string1 = "hello"
string2 = "world"
string3 = "python"

print(f"String '{string1}' reversed: {reverse_if_multiple_of_4(string1)}")
print(f"String '{string2}' reversed: {reverse_if_multiple_of_4(string2)}")
print(f"String '{string3}' reversed: {reverse_if_multiple_of_4(string3)}")