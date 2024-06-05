# Write a Python function that takes a list of words and returns the length of the longest one. 

def longest_word_length(words):

  if not words:
    return 0  # Handle empty list case

  longest_length = 0
  for word in words:
    if len(word) > longest_length:
      longest_length = len(word)
  return longest_length

# input 
words = input("Enter a list of words : ").split()

# print 
longest_length = longest_word_length(words)
print(f"The length of the longest word is: {longest_length}")