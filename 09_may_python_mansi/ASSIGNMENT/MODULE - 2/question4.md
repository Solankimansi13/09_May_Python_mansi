4. How memory is managed in Python? 
-> in python , there are basically two types of memory.
    1. stack memory 
    2. private memory
- all our references methods calls are stored in stack memory, whereas when we store any vlaue or an object then we make use of private heap memory, so this is the way these memory work.

for ex:-def func2(z):
            q = z +10
            return q
        def func1(x):
            z = x + 5
            p = func1(z)
            return p
        #main section
        x = 5
        y = func1(x)
        print(y)

        #20
explanation :- 
 when this function will be exicuted firstly the main function will be executed in that the first linne is x=5 that is x which is a reference will get stored in stack memory and 5 will be stored in heap memory which is being referred, 
 after that the second line is y=func1(x), as we know all the function are included in stack memory; so in this case , we will get the value of y which will be returned by the function so what will happen in this is function will get storedd in stack memory 
 the first line on function is z=x+5 here z will be storedd in func1 block of stack memorywhich will refer x+5 as value of x was 5 thus z will be referring to 10. so in this way, z is referring to 10.  
 the next line is p=func2(z). what will happen in this is p will be storred in func1 block of stack memory and another new block of func2 will be created in that the first line is q=z+10 , so in this case the q will be stored in the func2 block stack memory and it will refer to z+10 so the z was reffering to 10 ,q will refer to 20 because 10+10=20, after that the function 2 will return q. 
 so in this case the value of p will be 20. that is p will refer to 20 after this function 1 is returning p. so in this case as well the value of y will refeer to 20 
 so, in this case is all the extra variable will go in garbage collector. and in the end get the output y =20.
 so what does python interpreter do when no one is referring any object is start treating it as a dead object and this mechanism named as reference counting which means whenever an object becomes a dead object than that object automatically gets transferred to the garbage collector. 


- the allocation of heap space for python object is done by python memory manager. 
- the core API of python provides some tools for the programmer to code reliable and more rebust program.
- python also had build garbage collector which recycles all the unussed memory. 
- when an object is no longer referenced by the programmer, the heap space it coccupies can be freed.
- the garbage collector determines object which are no longer referrenced by the programs frees the occupied memory and make it available to heap space.

- the garbage gc module defines functions to eanble/ disable garbage collector.
    - gc.anable() - enables automatic garbage collection.
    - gc.disable() - disable automatic garbage collection.
    