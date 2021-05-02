# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 13:09:59 2021

@author: HP
"""

file = open("D:\PythonLessons\data.txt", "a")
file.write("Today I am learning about file operations\n")
file.close


file = open("D:\PythonLessons\data.txt", "r")
print(file.read())
file.close

print("")
file = open("D:\PythonLessons\data.txt", "r")
print(file.readline())
print("Name of file: " + file.name)
line=file.readline()
print("Read line %s" %(line))
pos=file.tell()
print("Current position: ", pos)

file.close


print("")
import pickle
pets_dict = {'Bob': 3, 'Jimmy': 2, 'Laika': 3, 'Jimmy': 10, 'Jack': 3, 'Stella': 3, 'Nzinga': 7 }
filename = 'pets'
outfile = open(filename, 'wb')
pickle.dump(pets_dict, outfile)
outfile.close()


print("")
infile = open(filename,'rb')
new_dict = pickle.load(infile)
print(new_dict)
print(new_dict==pets_dict)
print(type(new_dict))

infile.close()



