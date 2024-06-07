# How will you remove last object from a list? 
# Suppose list1 is [2, 33, 222, 14, and 25], what is list1 [-1]?
'''
to remove the last object from a list,we can use pop() method with the index -1. 
This will remove the last element from the list.
For example, if list1 is [2, 33, 222, 14, 25], then list1.pop(-1) will remove the last element, 
which is 25. After this operation, list1 will be [2, 33, 222, 14].
Regarding the second part of your question, list1[-1] refers to the last element in the list. 
So, if list1 is [2, 33, 222, 14, 25], then list1[-1] will return 25.

'''
# to print list1[-1]
list1 = [2, 33, 222, 14, 25]
print(list1[-1])
# to remove last elemeent from a list.
list1 = [2, 33, 222, 14, 25]
list1.pop(-1)
print(list1)