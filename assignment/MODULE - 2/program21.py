#  Write a Python function to reverses a string if its length is a multiple of 4. 

def reverse_if_multiple_of_4(text):
    if len(text) % 4 == 0:
        return text[::-1]
    else:
        return text

strings = []
for i in range(3):
    string = input(f"Enter string {i+1} :- ")
    strings.append(string)

for string in strings:
    print(f"String '{string}' reversed: {reverse_if_multiple_of_4(string)}")
