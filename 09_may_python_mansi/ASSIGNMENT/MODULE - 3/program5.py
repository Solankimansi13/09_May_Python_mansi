# How will you compare two lists? 


# 1. Equality:  

list1 = ['python', 'java','ruby']
list2 = ['python', 'java','ruby']
print(list1 == list2)  # Output: True

#----------------------------------------------------------------------------------------------------------

# 2. Element-wise comparison: 

list1 = ['python', 'java','ruby']
list2 = ['python', 'java','ruby']

result = True
for i in range(len(list1)):
	if list1[i] != list2[i]:
		result = False
		break
print(result)# Output: False

#---------------------------------------------------------------------------------------------------------------
# 3. Length comparison: 

list1 = ['python', 'java','ruby']
list2 = ['python', 'java']
print(len(list1) == len(list2))  # Output: False

#---------------------------------------------------------------------------------------------------------------

# 4. Subset comparison: 'python'
list1 = ['python', 'java','ruby']
list2 = ['python', 'java']
print(set(list2).issubset(set(list1)))  # Output: True