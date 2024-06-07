# # Write a Python program to count the number of characters (character frequency) in a string

print("statically")

string = "tops technology"
print(string.count('t'))


print("\n\n--------take input from the user----------------")

string = input(" Enter a string : ")

print("Enter (1) to perform total length and (2) for count of character.")

choice = input()
if choice == '1':
    print("total string length is : ", len(string))
elif choice == '2':
    char = input("Enter character to count :- ")
    if char in string:
        print(string.count(char))
    else:
        print("wrong input.")
else:
    print("Invalid choice.")