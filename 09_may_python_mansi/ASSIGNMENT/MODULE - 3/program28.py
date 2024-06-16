# Write a Python program to remove an empty tuple(s) from a list of tuples.

list1 = [(10,20,30),(40,50),(),(60,70,80)]
for tuple in list1:
    if(len(tuple) == 0):
        list1.remove(tuple)
print(list1)