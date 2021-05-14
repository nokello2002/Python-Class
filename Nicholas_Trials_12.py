# -*- coding: utf-8 -*-
"""
Created on Fri May  7 17:40:56 2021

@author: HP
"""
#using the regex module
print("")
import re
exp ="""hello there
I am from
opensourceIT2020"""
print(re.search(r"and", "Sun And Moon", flags=re.IGNORECASE))
print(re.findall(r"^\w", exp, flags= re.MULTILINE))


print("")
#python program showing how to use string modulo operator to print financier output
#print integer and floating value
print("OpenSourceIT2020 : %2d, Portal : %5.2f" %(1, 05.333))

#print integer value
print("Total students : %3d, ladies : % 2d" % (24000, 15000))

#print octal values
print("Printing octal value: ", "%7.3o" % (25))

print("Printing exponential value: ","%10.3E" % (356.08977))


print("")
for x in range (5):
    for y in range(x):
        print (y)
        
print("")        
#python program showing use of format() method
#using format() method
print("I love {} for {}!".format("OpenSourceIT2020", "what it does to us"))

print("")
#using format() method and refering to a position of the object
print("{0} and {1}".format("OpenSourceIT2020", "Portal"))
print("{1} and {0}".format("OpenSourceIT2020", "Portal"))

print("")
print(f"I love {'OpenSourceIT2020'} for \"{'what it does to us'}!\"")

print("")
print(f"{'OpensourceIT2020'} and {'Portal'}")


print("")
#python program showing use of format() method combining positional nad keyword arguments
print("Number one portal is {0}, {1}, and {other}.".format("OpenSourceIT2020", "For",
      other = "OpenSourceIT2020"))

#using format() method with number
print("OpenSourceIT2020 :{0:2d}, Portal:{1:8.2f}".format(12, 00.546))
print("")

#changing positional argument
print("Second argument: {1:3d}, first one: {0:7.2f}".format(47.42, 11))

print("")
print("OpenSourceIT2020: {a:5d}, Portal: {p:8.2f}".format(a=453, p=59.058))


print("")
#python program to show format () is used in dictionary
tab={"Open": 4007, "for": 3099, "Source": 8609738}
#using format () in dictionary
print("OpenSource: {0[Open]:d}; For: {0[for]:d}; OpenSourceIT2020: {0[Source]:d}".format(tab))

data=dict(fun = "OpenSourceIT for FREE", adj = "information")

#using format() in dictionary
print("I love {fun} computer {adj}".format(**data))

print("")
#python program to format output using string() method
cstr="I love OpenSourceIT2020"
#printing the center aligned string with fillchr
print("center aligned string with fillchr: ")
print(cstr.center(40, '#'))

print("")
#printing the left aligned string with "-" padding
print("the left aligned string is : ")
print(cstr.ljust(40, '-'))

print("")
#Printing the right aligned string with "-" padding
print("The right aligned string is : ")
print(cstr.rjust(40, '-'))


print("")
#code for disabling the softspace feature
print('G', 'M', 'N', sep='')

#for formatting a date
print("09","01","2020", sep='-')
#another example
print("BrendaO", "OpenSourceIT2020.store", sep='@')