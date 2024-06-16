# Write a Python program to check whether an element exists within a tuple. 

length = int(input("how many time you want to print  = "))
my_tuple = ()
for i in range(length):
    temp = int(input("enter tuple items = "))
    my_tuple = my_tuple + (temp,) #dds the input element to the tuple. 

element = int(input("what you want to check  = "))

index = -1
for i in range(len(my_tuple)):
    if my_tuple[i] == element:
        index = i
        break

if index != -1:
    print("tuple at index = ", index)
else:
    print("dont exist in tuple")