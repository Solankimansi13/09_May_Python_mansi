# Write a Python program to count the occurrences of each word in a given sentence 

sentence = input("Enter a sentence: ")
words = sentence.split()  

word_counts = {}  # Initialize an empty dictionary to store word counts

for word in words:
  if word in word_counts:
    word_counts[word] += 1  # Increment the count if the word exists
  else:
    word_counts[word] = 1  # Initialize the count to 1 if the word is new

print("Word counts:")
for word, count in word_counts.items():
  print(f"'{word}': {count}")