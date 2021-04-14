# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 09:47:40 2021

@author: HP
"""

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)
# returns True because z is the same object as x
print(x is y) #True
# returns False because x is not the same object as y, even if they have the same content
print(x == y) #False

# Python program to show
# bitwise operators
a = 10
b = 4
# Print bitwise AND operation	
print("a & b =", a & b) 
   
# Print bitwise OR operation 
print("a | b =", a | b) 
    
# Print bitwise NOT operation  
print("~a =", ~a) 
  
# print bitwise XOR operation  
print("a ^ b =", a ^ b) 



# Python program to show
# shift operators
  
a = 10
b = -10
  
# print bitwise right shift operator
print("a >> 1 =", a >> 1)
print("b >> 1 =", b >> 1)
  
a = 5
b = -10
  
# print bitwise left shift operator
print("a << 1 =", a << 1)
print("b << 1 =", b << 1)

print ("")
f = open("data.txt", 'w')  # Makes a new file in output mode
f.write("Habari \n") # Write this string of byte to the file
f.write("Yako \n")
f.close() # Close to flush memory buffers to disk

print("")
thisset = {"apple", "banana", "cherry"}
print(thisset)


print ("")
basket = ["apple", "orange", "apple", "pear", "orange", "banana"]
fruit = set(basket)  # create a set
print(fruit)
print("")
fruit=set(["orange", "pear", "apple", "banana"]) 
print ("orange" in fruit) # fast membership testing
print ("crabgrass" in fruit)


print("")
a = 5
print(a, "is of type", type(a))

a = 2.0
print(a, "is of type", type(a))

a = 1+2j
print(a, "is complex number?", isinstance(1+2j,complex))


print("")
num_int = 123 
num_flo = 1.23 
num_new = num_int + num_flo 
print("datatype of num_int:",type(num_int)) 
print("datatype of num_int:",type(num_flo)) 
print("Value of num_new:",num_new)
print("datatype of num_int:",type(num_new)) 

print ("")
dict([[1,2],[3,4]])
print (dict)

print ("")
# Python code to demonstrate Type conversion
# using int(), float()
# initializing string
string = "10010" 
# printing string converting to int base 2
converter = int(string,2)
print ("After converting to integer base 2 : ", end="")
print (converter)
# printing string converting to float
outcome = float(string)
print ("After converting to float : ", end="")
print (outcome)


print("")
num_int = 123
num_str = "456"

print("Data type of num_int:",type(num_int))
print("Data type of num_str:",type(num_str))



print("")
num_int = 123
num_str = "456"

print("Data type of num_int:",type(num_int))
print("Data type of num_str before Type Casting:", type(num_str))

num_str = int(num_str)
print("Data type of num_str after Type Casting:", type(num_str))
num_sum = num_int + num_str

print("Sum of num_int and num_str:", num_sum)
print("Data type of the sum:", type(num_sum))

print ("")
try:
      print(x)
except:
      print("An exception occurred")

print("")
try:
  print(m)
except NameError:
  print("Variable m is not defined")
except:
  print("Something else went wrong")
  
  
print("")
try:
   print(m)
except:
   print("Something went wrong")
finally:
   print("The 'try except' is finished")
   

print("")
try:
   f = open("demofile.txt")
   f.write("Lorum Ipsum")
except:
   print("Something went wrong when writing to the file")
finally:
   f.close()
   
print("")
x = -1
if x < 0:
    raise Exception("Sorry, no numbers below zero")





