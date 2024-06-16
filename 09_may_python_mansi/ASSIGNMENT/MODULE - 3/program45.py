'''
Write a Python program to create and display all combinations of letters, 
selecting each letter from a different key in a dictionary. 
Sample data: {'1': ['a','b'], '2': ['c','d']} 
Expected Output: 
ac ad bc bd
'''


dictionary = {'1': ['a', 'b'], '2': ['c', 'd']}

combinations = []

for letter1 in dictionary['1']:

	for letter2 in dictionary['2']:
		combinations.append(letter1 + letter2)
		
for combination in combinations:
	print(combination)