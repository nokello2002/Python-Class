# -*- coding: utf-8 -*-
"""
Created on Sat May 15 08:48:25 2021

@author: HP
"""

#program to generate mathematical tables
import pyfiglet

ascii_banner =pyfiglet.figlet_format("Multiplication Table")
print (ascii_banner)

def pypart(n):
    #print column headers
    for k in range (1, n):
        print (k, end ="\t")   
    print("______________________________________________")
    
    #print rows and data
    for i in  range(1, n):
        for j in range(1, n):
            print (i * j, end ="\t")
        print("\n")
    
#driver code
n=13
pypart(n)