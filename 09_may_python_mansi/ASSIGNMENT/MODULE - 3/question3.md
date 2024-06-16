3. Differentiate between append () and extend () methods? 

 The append() and extend() methods are use to add element in list.

append():

- Add a single element to end of list.
- If the element is a list, it will add a single element (a sublist).
- Example: 
            my_list.append(5) or my_list.append([5, 6])

extend():

- Add multiple elements to the end of list.
- If the element is a list, it will unpack and its elements will added individually.
- Example:
            my_list.extend([5, 6]) 
                        or
            my_list.extend((5, 6))

 example of  difference:

my_list = [1, 2, 3]

- my_list.append(4) will result in [1, 2, 3, 4]
- my_list.append([4, 5]) will result in [1, 2, 3, [4, 5]] (notice the sublist)
- my_list.extend([4, 5]) will result in [1, 2, 3, 4, 5]
- my_list.extend((4, 5)) will also result in [1, 2, 3, 4, 5]

- append() adds a single element, while extend() adds multiple elements. 
- If you pass a list to append(), it will be added as a sublist, while extend() will unpack the list and add its elements individually.
- append() adds a single element to the end of the list. while extend() adds multiple elements to the end of the list.
- If a list is passed as an argument to append(), it will be added as a sublist. but if list is pass as an argument to extend(), it will be unpack and its element will be add individually.