# Write a Python program to convert a list of tuples into a dictionary. 


tuples_list = [("mansi", 13), ("shubham", 21), ("dhara", 19)]

# Create empty dictionary
dictionary = {}

for tuple in tuples_list:

	key, value = tuple

	dictionary[key] = value

print(dictionary) 
