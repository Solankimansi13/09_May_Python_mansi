#  Write a Python program to check whether a list contains a sub list 



n = input("Enter how many values you want to print: ")


main_list = ""
for i in range(int(n)):
	main_list += input("Enter value: ")

n = input("Enter number of element in sub list: ")

sub_list = ""
for i in range(int(n)):
	sub_list += input("Enter value: ")

found = 0
for item in sub_list:
	if item in main_list:
		found = found + 1

if found == len(sub_list):
	print("list contains sub list")
else:
	print("list not contain sub list")
