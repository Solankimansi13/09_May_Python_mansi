# Write a Python script to merge two Python dictionaries 


 
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

dict1.update(dict2)

print(dict1)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}


# Using ** operator:

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

merged_dict = {**dict1, **dict2}

print(merged_dict) 