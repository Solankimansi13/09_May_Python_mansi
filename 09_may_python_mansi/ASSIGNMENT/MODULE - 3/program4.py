# Write a Python function to get the largest number, smallest num and sum of all from a list. 

def get_number(number):#create a function get_number with argument and return result of number
    largest = number[0]#for largest number 
    smallest = number[0]#for smallest number
    total = 0#variable store sum of all numbers in the list.
    for i in number:#i for itratration
        if i > largest:#if the number is grater than lagest 
            largest = i#assign largest in to i
        elif i < smallest:#same like largest number
            smallest = i
        total = total + i
    return largest, smallest, total#this will return small, large and sum 

number = input("Enter numbers = ")
number_list = []#initialize empty to store the converted integer values.
for x in number.split():#this will split each integer by space.
    number_list.append(int(x))#converrt each string to an integer

largest, smallest, total = get_number(number_list)#call function and assign value in largest , smallest , and total
print("Largest:", largest)#print largest number
print("Smallest:", smallest)#print samallest number 
print("Sum:", total)#print total
