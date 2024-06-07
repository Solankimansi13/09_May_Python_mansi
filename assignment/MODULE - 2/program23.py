# Write a Python function to insert a string in the middle of a string.

def insert_string_middle(real, add):
    middle = len(real) // 2
    return real[:middle] + add + real[middle:]

# Example usage:
main = input("Enter the original string: ")
add = input("Enter the string to insert: ")

result = insert_string_middle(main, add)
print(result)
