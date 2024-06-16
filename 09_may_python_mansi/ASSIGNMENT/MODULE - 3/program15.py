# Write a Python program to get unique values from a list 

list = ['python','java','c','c','java','python','ruby','pyhton']
l1 = []
for i in list:
    if i not in l1:
        l1.append(i)
print("given list = ", list)
print("unique list = ",l1)