# Write a Python program to check multiple keys exists in a dictionary 

def check_keys(dictionary, keys):

	for key in keys:

		if key not in dictionary:
			return False
	return True

dictionary = {"name": "mansi", "age": 23, "city": "rajkot"}
keys = ["name", "age", "city"]


if check_keys(dictionary, keys):
	print("All keys exist in the dictionary")
else:
	print(" does not exist in the dictionary")

