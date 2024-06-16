# Write a Python script to print a dictionary where the keys are numbers between 1 and 15.



dictionary = {}

for i in range(1, 16):

	square = i ** 2
	dictionary[i] = square

print(dictionary)