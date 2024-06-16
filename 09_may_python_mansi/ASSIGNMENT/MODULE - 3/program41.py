# Write a Python program to map two lists into a dictionary

# Define two lists
keys = ['a', 'b', 'c', 'd']
values = [1, 2, 3, 4]


dictionary = {}

for i in range(len(keys)):
    dictionary[keys[i]] = values[i]

print(dictionary)  