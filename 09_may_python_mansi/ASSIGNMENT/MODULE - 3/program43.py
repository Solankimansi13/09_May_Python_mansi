# Write a Python program to print all unique values in a dictionary.

dictionary = {'a': 1, 'b': 2, 'c': 2, 'd': 3, 'e': 3, 'f': 3}

unique_values = set(dictionary.values())

for value in unique_values:
    print(value)