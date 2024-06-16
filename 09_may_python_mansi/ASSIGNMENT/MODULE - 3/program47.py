'''
 Write a Python program to combine values in python list of dictionaries. 
Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 
300}, o {'item': 'item1', 'amount': 750}] 
Expected Output: 
Counter ({'item1': 1150, 'item2': 300})
'''

data = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]

combined_values = {}

for dictionary in data:

	item = dictionary['item']
	amount = dictionary['amount']


	if item in combined_values:
		combined_values[item] += amount
	else:
		combined_values[item] = amount

for item, amount in combined_values.items():
	print(f"{item}: {amount}")
