# Write a Python program to replace last value of tuples in a list. 


tuples_list = [(10, 20, 30), (40, 50, 60), (70, 80, 90)]

new_last_value = 100


new_tuples_list = []


for tuple in tuples_list:
	new_tuple = tuple[-1] + (new_last_value,)
	new_tuples_list.append(new_tuple)


print(new_tuples_list)