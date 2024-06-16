# Write a Python script to check if a given key already exists in a dictionary

dict = {1:10 , 2:20 , 3:30 , 4:40 ,5:50}
def is_key_present(x):
    if x in dict:
        print("key is present in the dictionary.")
    else:
        print("key is notpresent in the dictionary.")

is_key_present(9)
is_key_present(2)