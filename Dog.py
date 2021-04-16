# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 11:17:37 2021

@author: HP
"""

class Dog:
    species = "Canis familiaris"
    def __init__(self, name, breed, color, age):
        self.name = name
        self.breed = breed
        self.color = color
        self.age = age
    # Instance method
    def description(self): #1
        return f"{self.name} is {self.age} years old"
    # Another instance method
    def speak(self, sound):#2
        return f"{self.name} says {sound}"
    
    def __str__(self): #1
        return f"{self.name} is {self.age} years old"
    
Jimmy = Dog("Jimmy","Golden Retriever","Light Golden", 6)
Jack = Dog("Jack","german shepherd","Black & Tan", 4)
Tobi = Dog("Tobi","cocker spaniel","Black", 2)


print(Tobi.color)
print(Jimmy.breed)
print(Jack.age)
print(Tobi.species)
Jack.age=15
print(Jack.age)

Jack=Dog("Jack","Golden Retriever","Light Golden",6)
print(Jack.description())
print(Jack)


print ("")
print("")

