# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def absolute_value(number):
    """This function returns the absolute
    value of the entered number"""
    if number >= 0:
        return number
    else:
        return -number
print(absolute_value(4))
print(absolute_value(-6))

print("")
def my_function(x):
  return 5 * x
print(my_function(3))
print(my_function(5))
print(my_function(9))


print("")
# The wonderful Jackson 5
def my_function(firstname):
  print(firstname + " Jackson")
print(my_function("Jackie"))
print(my_function("Tito"))
print(my_function("Jermaine"))
print(my_function("Marlon"))
print(my_function("Michael"))

print("")
def my_function(*presidents):
  print("The name of the first president of Ghana was: " + presidents[2])
print (my_function("Dr. Kenneth Kaunda", "Mwalimu Julius Nyerere", "Dr. Kwame Nkrumah"))

print("")
def my_function(Engi3, Engi2, Engi1):
  print("The youngest Scientist was: " + Engi3)

print(my_function(Engi1 = "Galileo", Engi2 = "Newton", Engi3 = "Einstein"))


print("")
def my_function(**activist):
  print("His last name was: " + activist["lname"])

print(my_function(fname = "Malcolm", lname = "X"))


print("")
def my_function(country = "Tanzania"):
  print("I am from " + country)

print(my_function("Kenya"))
print(my_function("Uganda"))
print(my_function())
print(my_function("Somalia"))


print("")
def my_function(politicians):
  for x in politicians:
    print(x)
mashuja = ["Tom Mboya", "J.M. Kariuki", "Argwings Kodhek","Dr.R. Ouko"]

print(my_function(mashuja))

print("")
def my_func():
	x = 10
	print("Value inside function:",x)
x = 20
my_func()
print("Value outside function:",x)

print("")
# Program to show the use of lambda functions
double = lambda x: x * 2

print(double(5))


print("")
def double(x):
   return x * 2

print(double(5))


print("")
# Program to filter out only the even items from a list
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(filter(lambda x: (x%2 == 0) , my_list))
print(new_list)


print("")
# Program to double each item in a list using map()
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(map(lambda x: x * 2 , my_list))
print(new_list)


print("")
x = lambda a : a + 10
print(x(5))


print("")
x = lambda a, b : a * b
print(x(5, 6))


print("")
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))


print("")
# Program to illustrate
# the use of user-defined functions

def add_numbers(x,y):
   sum = x + y
   return sum

num1 = 5
num2 = 6

print("The sum is", add_numbers(num1, num2))


print("")
def get_products(x,y):
    product=x * y
    return product

#first_num=int(input("Enter first number: "))
#second_num=int(input("Enter second number: "))
first_num=58
second_num=78
print("Result: ", get_products(first_num,second_num))


print("")
def list_benefits(benefits):
    for x in benefits:
        print (x)
        
merit=["More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"]
print(list_benefits(merit))    


print("")
def build_sentence(info):
    sentence=info + " " + " is a benefit of functions!"
    print (sentence)

maneno="Python"
print(build_sentence(maneno) )




