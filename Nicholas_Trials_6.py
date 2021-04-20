# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 09:15:20 2021

@author: HP
"""

total_cost = 1 + 3 * 4
print(total_cost)

print("")
cities = ["Atlanta", "Baltimore", "Chicago",
"Denver", "Los Angeles", "Seattle"]
smaller_list_of_cities = cities[2:5]
print(smaller_list_of_cities)
smaller_list_of_cities = cities[:5]
print(smaller_list_of_cities)
smaller_list_of_cities = cities[2:]
print(smaller_list_of_cities)

del cities[2]
print(cities)
cities.remove("Denver")
print(cities)

print ("")
city_to_check = "Tucson"
cleanest_cities = ["Cheyenne", "Santa Fe", "Tucson",
"Great Falls", "Honolulu"]
for x in cleanest_cities:
    if x==city_to_check:
        print("Cleanest city: " + city_to_check)
    else:
        print("Dirty city:" + x)
        

print("")
customer_29876 = {"first name": "David", "last name": "Elliott", "address": "4803 Wellesley St."}

print(customer_29876["address"])
cust_address=customer_29876["address"]
print(cust_address)

print("")
for each_value in customer_29876.values():
  print(each_value)

print("")  
for each_key in customer_29876.keys():
 print(each_key)
 
print("")
for each_key, each_value in customer_29876.items():
    print("The customer's " + each_key + " is " + each_value)
    
    
print("")
customers = {
 0: {
     "first name":"John",
     "last name": "Ogden",
     "address": "301 Arbor Rd.",
     },
 1: {
     "first name":"Ann",
     "last name": "Sattermyer",
     "address": "PO Box 1145",
     },
 2: {
     "first name":"Jill",
     "last name": "Somers",
     "address": "3 Main St.",
     },
 }

print("")
print(customers[2])
print(customers[2]["address"])

print("")
def add_numbers(first_number, second_number):
    total = first_number + second_number
    print("The total is " + str(total))

print("")
first=float(input("Enter first number: "))
second=float(input("Enter second number:"))
add_numbers(first,second)


print("")
with open("greet.txt", "w") as f:
    f.write("Hello, world!")
    
    
print("")
with open("greet.txt", "r") as f:
    text_of_file = f.read()

print (text_of_file)

print("")
with open("greet.txt", "a") as f:
    f.write("\nHave a nice day!")
    
print("")
with open("greet.txt", "r") as f:
    text_of_file = f.read()

print (text_of_file)


print("")
import csv
with open("whatever.csv", "w", newline="") as f:
    data_handler = csv.writer(f, delimiter=",")
    data_handler.writerow(["Year", "Event", "Winner"])
    data_handler.writerow(["1995", "Best-Kept Lawn", "None"])
    data_handler.writerow(["1999", "Gobstones", "Welch National"])
    
print("")
with open("whatever.csv", "a", newline="") as f:
    data_handler = csv.writer(f, delimiter=",")
    data_handler.writerow(["2006", "World Cup", "Burkina Faso"])
    data_handler.writerow(["2011", "Butter Cup", "France"])
    data_handler.writerow(["2012", "Coffee Cup", "Brazil"])

 
