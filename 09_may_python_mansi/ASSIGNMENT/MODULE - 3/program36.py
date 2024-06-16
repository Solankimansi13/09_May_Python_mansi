#  How Do You Check The Presence Of A Key In A Dictionary? 

# 1. Using the in keyword:


dictionary = {"name": "mansi", "age": 23}

if "name" in dictionary:
    print("Key is present")
else:
    print("Key is not present")

print('-------------------------------------------------')


# 2. Using the get() method:
dictionary = {"name": "mansi", "age": 23}

if dictionary.get("name") is not None:
    print("Key is present")
else:
    print("Key is not present")
print('-------------------------------------------------')


# 3. Using the keys() method:
dictionary = {"name": "mansi", "age": 23}

if "name" in dictionary.keys():
    print("Key is present")
else:
    print("Key is not present")

print('-------------------------------------------------')


# 4. Using the has_key() method (Python 2 only):
dictionary = {"name": "mansi", "age": 23}

if dictionary.has_key("name"):
    print("Key is present")
else:
    print("Key is not present")
