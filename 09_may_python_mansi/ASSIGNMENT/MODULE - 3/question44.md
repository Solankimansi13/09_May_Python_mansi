44.  Why Do You Use the Zip () Method in Python? 

- The zip() method in Python is used to combine two or more lists into a single list of tuples, 
- where each tuple contains one element from each of the original lists. -

- used

1. Pairing elements: To pair elements from two lists, such as pairing names with ages or IDs.
2. Parallel iteration: To iterate over two or more lists simultaneously, making it easy to perform operations on corresponding elements.
3. Data alignment: To align data from multiple lists into a single data structure, making it easier to work with.
4. Creating dictionaries: To create dictionaries by zipping keys with values.
5. Data transformation: To transform data from multiple lists into a new format, such as converting two lists into a list of tuples.

-  example:

names = ['John', 'Mary', 'David']
ages = [25, 31, 42]

zipped = zip(names, ages)
print(list(zipped))  # Output: [('John', 25), ('Mary', 31), ('David', 42)]
