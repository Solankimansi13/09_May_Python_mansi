# Write a Python program to find the repeated items of a tuple.

tuple1 = (1,2,3,4,5,6,1,2,3,8,10)
list1 = []

for i in tuple1:
    if tuple1.count(i) > 1:
        if i not in list1:
            list1.append(i)

print(list1)