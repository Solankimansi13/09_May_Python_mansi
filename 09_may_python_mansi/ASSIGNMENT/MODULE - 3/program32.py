# Write a Python script to sort (ascending and descending) a dictionary by value. 



dictionary = {"python": 1, "java": 2, "ruby": 3, "kotlin": 4}

# Sortascending order
sorted_dictionary_ascending = dict(sorted(dictionary.items(), key=lambda item: item[1]))

# Sort descending order
sorted_dictionary_descending = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))

print("Ascending Order:", sorted_dictionary_ascending)
print("Descending Order:", sorted_dictionary_descending)

