# How Do You Traverse Through A Dictionary Object In Python?

'''
There are several ways to traverse through a dictionary object in Python:
1. Using the keys() method: 
This method returns a list of all the keys in the dictionary. You can then iterate over this list to access each key-value pair.
for key in dictionary.keys():
    print(key, dictionary[key])
2. Using the values() method: 
This method returns a list of all the values in the dictionary. You can then iterate over this list to access each value.
for value in dictionary.values():
    print(value)
3. Using the items() method: 
This method returns a list of tuples, where each tuple contains a key-value pair. You can then iterate over this list to access each key-value pair.
for key, value in dictionary.items():
    print(key, value)
4. Using a for loop: 
You can directly iterate over the dictionary using a for loop, which will iterate over the keys.
for key in dictionary:
    print(key, dictionary[key])
5. Using the iterkeys(), itervalues(), and iteritems() methods: These methods return iterators over the keys, values, and key-value pairs respectively. They are more memory efficient than the keys(), values(), and items() methods.
for key in dictionary.iterkeys():
    print(key)
for value in dictionary.itervalues():
    print(value)
for key, value in dictionary.iteritems():
    print(key, value)
'''


# 1. Using the keys() method:
dictionary = {"mansi": 30, "riya": 25, "dhara": 35}

for key in dictionary.keys():
    print(key)  

#---------------------------------------------------------------------------------------------------------------#
# 2. Using the values() method:
dictionary = {"mansi": 30, "riya": 25, "dhara": 35}

for value in dictionary.values():
    print(value)  

#---------------------------------------------------------------------------------------------------------------#

# 3. Using the items() method:
dictionary = {"mansi": 30, "riya": 25, "dhara": 35}

for key, value in dictionary.items():
    print(key, value) 


#---------------------------------------------------------------------------------------------------------------#

# 4. Using a for loop:
dictionary = {"mansi": 30, "Alice": 25, "Bob": 35}

for key in dictionary:
    print(key, dictionary[key])  

#---------------------------------------------------------------------------------------------------------------#

# 5. Using the iterkeys(), itervalues(), and iteritems() methods (Python 2 only):
dictionary = {"John": 30, "Alice": 25, "Bob": 35}

for key in dictionary.iterkeys():
    print(key) 

for value in dictionary.itervalues():
    print(value) 

for key, value in dictionary.iteritems():
    print(key, value)  

