# # Write a Python program to find the first appearance of the substring 
# 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the 
# whole 'not'...'poor' substring with 'good'. Return the resulting string. 


text = input("Enter a string: ")

not_index = text.find('not')
poor_index = text.find('poor')

if (not_index != -1 and poor_index != -1 and not_index < poor_index):
  text = text.replace(text[not_index:poor_index + 4], 'good')

print(f"Resulting string: {text}")