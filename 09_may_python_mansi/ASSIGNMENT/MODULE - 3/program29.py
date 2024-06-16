# Write a Python program to unzip a list of tuples into individual lists. 


tuples_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

# Use zip function to unzip list of tuples
list1, list2, list3 = zip(*tuples_list)

# Print the individual lists
print(list(list1))  
print(list(list2)) 
print(list(list3)) 