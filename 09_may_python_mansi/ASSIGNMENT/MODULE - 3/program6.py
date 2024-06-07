'''
Write a Python program to count the number of strings where the string 
length is 2 or more and the first and last character are same from a given 
list of strings. 
'''

n = 0 
list1=['SOS','121','python','131','tops']
for i in list1:
    if len(i)>1 and i[0] == i[-1]:
        print("the given words are = ",i)
        n = n+1
print("no. of wrds you want",n)