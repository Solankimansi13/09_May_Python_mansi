1. What is List? How will you reverse a list?

- list is a collection of item.  
- list has different data types  :- strings, integers, floats, etc... 
- list defined in [] brakets. and elements are separated with comma. 

- For example:

    my_list = ['java','python','c++','javascript']

- To reverse a list, there are use reverse() method or slicing.

- for examples :

Method 1: reverse() method

 my_list = ['java','python','c++','javascript']
 my_list.reverse()
 print(my_list) 
 # Output: ['javascript','c++','python','java']


Method 2: Using slicing

 my_list = ['java','python','c++','javascript']
 reversed_list = my_list[::-1]
 print(reversed_list)
  # Output: ['java','python','c++','javascript']

- Slicing create a new list with the elements in reverse format. 
- [::-1] this will start from end of list and start from last element  and step back  by 1 element every time.

- result will be same in both method.