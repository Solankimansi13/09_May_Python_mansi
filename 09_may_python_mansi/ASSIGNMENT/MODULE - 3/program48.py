'''
Write a Python program to create a dictionary from a string. 
 
Note: Track the count of the letters from the string. 
Sample string: 'w3resource' 
Expected output: 
{'3': 1,'s: 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}
'''


string = 'w3resource'

letter_counts = {}

for character in string:

	if character in letter_counts:
		letter_counts[character] += 1

	else:
		letter_counts[character] = 1

for key, value in letter_counts.items():
	print(f"{key}: {value}")
