# Write a Python program to count the occurrences of each word in a given sentence 

def count_words():
    sentence = input("Enter a sentence: ")
    count = {}
    for word in sentence.split():
        word = word.strip('.,!@#$%&*').lower()
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return count

print(count_words())
