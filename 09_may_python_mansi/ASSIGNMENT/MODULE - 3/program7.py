# Write a Python program to remove duplicates from a list. 

a = ['python','java','php','ruby','r','python','java']

same_element = set()
diff_element = []

for i in a:
    if i not in same_element:
        diff_element.append(i)
        same_element.add(i)
print(same_element)

# second method
# taking input from the user

n = int(input("Enter the number of items: "))

items = []

for i in range(n):
    item = input(f"Enter item : ")
    i = i+1
    
    if item not in items:
        items.append(item)

print("after removing duplicate",items)