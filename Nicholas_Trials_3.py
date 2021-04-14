# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 11:42:47 2021

@author: HP
"""

flag = True
if flag==True:
    print("Welcome")
    print("To The")
    print("Largest Python Class in Sub-Saharan Africa")


print ("")
number = 33
if number % 2 != 0:
    print("Even Number")
else:
    print("Odd Number")
    

print ("")
number = 1122
if 9 < number < 99:
    print("Two digit number")
elif 99 < number < 999:
    print("Three digit number")
elif 999 < number < 9999:
    print("Four digit number")
else:
    print("number is <= 9 or >= 9999")


print ("")
# Program to print squares of all numbers present in a list
# List of integer numbers
numbers = [1, 2, 4, 6, 11, 20]
# variable to store the square of each num temporary
sq = 0

# iterating over the given list
for val in numbers:
    # calculating square of each number
    sq = val * val
    # displaying the squares
    print(sq)



print("")
fruits = ["apple", "banana", "cherry", "Avocado", "Mango"]
for fruit in fruits:
  print(fruit)
  

print("")
for fruit in "Pinneaple":
  print(fruit)


print("")
for a in "adabracadabra":
    print(a)
    

print ("")
fruits = ["Lemon", "apple", "banana", "Avocado", "cherry","Papaya"]
for fruit in fruits:
  if fruit == "Avocado":
    continue
  print(fruit)


print("")
for fruit in range(3, 10):
  print(fruit)


print("")
for fruit in range(3, 50, 4):
  print(fruit)


print("")
for fruit in range(10):
  print(fruit)
else:
  print("Finally done!")


print("")
adjective = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for describe in adjective:
  for name in fruits:
    print(describe, name)


print("")
for x in [0, 1, 2, 3, 4]:
  pass


print("")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)


print("")
index = 1
while index < 10:
  print(index)
  index += 1


print("")
index = 1
while index < 6:
  print(index)
  if index == 3:
    break
  index += 1


print("")
index = 0
while index < 6:
  index += 1
  if index == 3:
    continue
  print(index)


print("")
index = 1
while index < 6:
  print(index)
  index += 1

    

