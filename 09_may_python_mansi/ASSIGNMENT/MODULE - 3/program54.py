#  How can you pick a random item from a list or tuple?

# To pick a random item from a list or tuple, you can use the random module in Python. Here's an example program:

import random

my_list = [1, 2, 3, 4, 5]
random_item = random.choice(my_list)
print("Random item from the list:", random_item)


#  the random.choice() function can also be used with tuples:
import random

my_tuple = (1, 2, 3, 4, 5)

random_item = random.choice(my_tuple)

print("Random item from the tuple:", random_item)

# This will also pick a random item from the tuple and print it to the console.
