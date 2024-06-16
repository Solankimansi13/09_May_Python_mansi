# Write a Python program to find the highest 3 values in a dictionary 


dictionary = {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50, 'f': 60}

values = []

for key, value in dictionary.items():
    values.append(value)

values.sort(reverse=True)

for i in range(3):
    for key, value in dictionary.items():
        if value == values[i]:
            print(f"{key}: {value}")
            break
