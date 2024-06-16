# Write a Python script to concatenate following dictionaries to create a new one.

#pre defined dictionary

a = {1:10, 2:20}
b = {3:30, 4:40}
c = {5:50, 6:60 ,7:70}

#empty dictionary
e = {}

#printing pre define dictionaries

print ("a = ",a)
print ("b = ",b)
print ("c = ",c)

#concatinating dictionary

for i in (a,b,c):
    e.update(i)

#print new dictionary 

print(e)
