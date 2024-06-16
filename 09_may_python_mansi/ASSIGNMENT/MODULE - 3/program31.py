#  How will you create a dictionary using tuples in python? 



tuples_list = [("python", 1), ("java", 2), ("c", 3)]#list of tuple
dictionary = {}#empty dictionary

for tuple in tuples_list:
	key, value = tuple

	dictionary[key] = value


print(dictionary)  
