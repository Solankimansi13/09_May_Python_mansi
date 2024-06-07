#Write a Python program to get the Fibonacci series of given range.
'''
f0 =0
f1= f0+ 1
f2= f0 +f1
f3 = f2+f1
f4= f3 + f2 
'''


a = 0
b = 1
number = int(input("which number of fibonaci series you want = "))

if number == 1:
    print(a)
else:
    print(a)
    print(b)
    for i in range(1,number+1):
        c = a + b
        a = b
        b = c
        print(c)