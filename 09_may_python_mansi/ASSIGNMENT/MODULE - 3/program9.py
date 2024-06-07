#  Write a Python function that takes two lists and returns true if they have at least one common member.

def func1(list1, list2):
    common = 0
    for i in list1:
        if i in list2:
            common += 1
    return common

def get_list():
    n = int(input("enter how many number you want to print = "))
    my_list = []
    for i in range(n):
        temp = int(input("enter list item = "))
        my_list.append(temp)
    return my_list

first = get_list()
second = get_list()
total = func1(first, second)
print("the number of common member is = ", total)