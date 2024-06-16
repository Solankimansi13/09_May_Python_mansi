# How will you remove last object from a list? 
# Suppose list1 is [2, 33, 222, 14, and 25], what is list1 [-1]?
'''
to remove the last object from a list, pop() method use with index -1. 
This remove last element in the list.
For example, 
if list1 is [10,20,30,40,50], 
list1.pop(-1) will remove last element, that is 50. 
After that list1 will be [10,20,30,40]
'''

'''
second part of question, 
list1[-1] is last element in list. 
list1 is [2, 33, 222, 14, 25], then list1[-1] is 25.

#output :
25
'''
 


list1 = [2, 33, 222, 14, 25]
print(list1[-1])

# remove last elemeent from a list.

list1 = [2, 33, 222, 14, 25]
list1.pop(-1)
print(list1)


