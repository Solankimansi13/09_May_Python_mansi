#  Write a Python function that takes two lists and returns true if they have at least one common member.

def check_common(first,second):
    for i in first:
        if i in second:
            return True
    return False

length = int(input("Enter List 1 Length = "))
list1 = []
for i in range(length):
    temp = int(input("Enter List 1 Item = "))
    list1.append(temp)

length = int(input("Enter List 2 Length = "))
list2 = []
for i in range(length):
    temp = int(input("Enter List 2 Item = "))
    list2.append(temp)

if check_common(list1,list2):
    print("one comman menber exist between two lists")
else:
    print("no coomon menber exist between two list. ")