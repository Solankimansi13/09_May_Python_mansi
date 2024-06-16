'''
Write a Python function that checks whether a passed string is 
palindrome or not
'''

def is_palindrome(s):
    s = s.replace(" ", "").lower()  # remove spaces and convert to lowercase
    length = len(s)
    for i in range(length // 2):
        if s[i] != s[length - i - 1]:
            return False
    return True

string = input("Enter a string: ")
if is_palindrome(string):
    print(f'"{string}" is a palindrome')
else:
    print(f'"{string}" is not a palindrome')
