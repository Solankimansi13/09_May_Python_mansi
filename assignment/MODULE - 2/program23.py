# Write a Python function to insert a string in the middle of a string.

def insert_string_middle(original_string, string_to_insert):
 
  middle_index = len(original_string) // 2
  return original_string[:middle_index] + string_to_insert + original_string[middle_index:]

# Example usage:
original_string = "mi"
string_to_insert = "ans"

result = insert_string_middle(original_string, string_to_insert)
print(f"Result: {result}")