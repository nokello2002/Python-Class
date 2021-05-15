# -*- coding: utf-8 -*-
"""
Created on Sat May 15 08:37:33 2021

@author: HP
"""

#Python 3.x code to demonstrate the star patter
#Function to demonstrate printing pattern

def pypart(n):
    #outer loop to handle number of rows
    #n in this case
    for i in range (0, n):
        #inner loop to handle the number of columns
        #values changing according to outer loop
        for j in range (0, i +1):
            #printing stars
            print("* ", end="")
        #ending line after each row
        print("\r")
        
#Driver code
n=10
pypart(n)
