# Write a Python function that takes a list and returns a new list with unique elements of the first list.


def uniqueLst(Dat1):
    x= []
    for p in Dat1:
        if p not in x:
            x.append(p)
    return x
dataList= []
n = int(input("enter total element in a list = "))
for k in range(n):
    data= int(input("enter in data list = "))
    dataList.append(data)

print("originl list ", dataList)
print(uniqueLst(dataList))