# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 11:58:49 2021

@author: HP
"""

class ComplexNumber:
    def __init__(self, r=0, i=0):
        self.real = r
        self.imag = i

    def get_data(self):
        print(f'{self.real}+{self.imag}j')


# Create a new ComplexNumber object
num1 = ComplexNumber(2, 3)

# Call get_data() method
# Output: 2+3j
num1.get_data()

# Create another ComplexNumber object
# and create a new attribute 'attr'
num2 = ComplexNumber(5)
num2.attr = 10

# Output: (5, 0, 10)
print((num2.real, num2.imag, num2.attr))

# but c1 object doesn't have attribute 'attr'
# AttributeError: 'ComplexNumber' object has no attribute 'attr'
print(num2.attr)


print("")
print("")
class Student:
    def __init__(self,name, grade, email, phone, gender, age):
        self.name=name
        self.grade=grade
        self.email=email
        self.phone=phone
        self.gender=gender
        self.age=age
        
    def myfunct(self):
        print("Habari yako " + self.name)
        
stu=Student("Lucy Auma", "10th Grade", "l.auma@gmail.ke", "020546 5875", "Female", 25)
print(stu.name)
print(stu.grade)
print(stu.email)
print(stu.phone)
print(stu.gender)
print(stu.age)

print("")
stu.myfunct()

print("")
print("")
class House:
    def __init__(self, Type, age, material,roof, color):
        self.Type=Type
        self.age=age
        self.material=material
        self.roof=roof
        self.color=color
        
    def house_def(self):
        print("The " + self.color + " house is " + self.age + " years old - It has " + self.roof + " roof top, It is a " + self.Type)
    
red_house=House("bungalow", "15", "brick", "corrugated", "red")
pink_house=House("family unit", "20", "wood", "corrugated", "pink")

red_house.house_def()
pink_house.house_def()

        

