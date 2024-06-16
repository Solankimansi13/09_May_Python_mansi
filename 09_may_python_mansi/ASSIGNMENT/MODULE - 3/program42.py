'''
Write a Python program to combine two dictionary adding values for 
common keys. 
d1 = {'a': 100, 'b': 200, 'c':300} o d2 = {'a': 300, 'b': 200,'d':400} 
Sample output: Counter ({'a': 400, 'b': 400,'d': 400, 'c': 300}). 
'''


dict1 = {'a': 100, 'b': 200, 'c': 300}
dict2 = {'a': 300, 'b': 200, 'd': 400}

dict3 = {}

for key, value in dict1.items():
	dict3[key] = value
for key, value in dict2.items():

	if key in dict3:
		dict3[key] += value
	else:
		dict3[key] = value

print(dict3) 