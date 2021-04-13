# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 18:50:34 2021

@author: HP
"""

mystring = 'Hello World!'
print (mystring)
mystring = "hello there"
print (mystring)
# change this code
mystring = "hello"
myfloat=10.00
myint = 20
if mystring == "hello":
    print("String: %s" % mystring)
    if isinstance(myfloat, float) and myfloat == 10.0:
        print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)
    
    
str = 'Hello World!'
print (str)
print(str[0])
print(str[2:5])
print(str[2:])
print(str * 2)
print(str + "test case")


list = [ 'abcd3', 886 , 3.25, 'Jonathan', 90.3 ]
tinylist = [1123, 'George']
print (list)          # Prints complete list (correct in Python 2.7)
print (list)         # Prints complete list (correct as from Python 3.x and above)
print (list[0])       # Prints first element of the list
print (list[1:3])     # Prints elements starting from 2nd to 3rd 
print (list[2:])      # Prints elements starting from 3rd element
print (tinylist * 2)  # Prints list two times
print (list + tinylist) # Prints concatenated lists


mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0]) # prints 1
print(mylist[1]) # prints 2
print(mylist[2]) # prints 3
# prints out 1,2,3
for x in mylist:
    print(x)


numbers = []  
strings = []
names = ["John", "Eric", "Jessica"]
# write your code here
second_name = None
# this code should print out the filled arrays and the second name in the names list (Eric).
numbers.append(1)
numbers.append(2)
numbers.append(3)

strings.append("Hello")
strings.append("World")
second_name=names[1]
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)

tuple = ( 'abcd',586 ,3.23, 'Rebecca',70.3  )
tinytuple = (123, 'Kamau')
print (tuple)               # Prints the complete tuple
print (tuple[0] )           # Prints first element of the tuple
print (tuple[1:3])        # Prints elements of the tuple starting from 2nd till 3rd 
print (tuple[2:])       # Prints elements of the tuple starting from 3rd element
print (tinytuple * 2)       # Prints the contents of the tuple twice
# Prints concatenated tuples
print (tuple + tinytuple) 


dict = {}
dict['one'] = "This is number one"
dict[2]     = "This is number two"
tinydict = {'name': 'Henry','code':6733, 'dept': 'IT'}
print (dict['one'])       # Prints value for 'one' key
print (dict[2])           # Prints value for 2 key
print (tinydict)          # Prints complete dictionary
print (tinydict.keys())   # Prints all the keys
print (tinydict.values()) # Prints all the values

Colors = {'Tamara': 'Pink', 
           'Sarah': 'Red', 
           'Odero': 'Blue'} 
print (Colors)





