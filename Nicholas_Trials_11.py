# -*- coding: utf-8 -*-
"""
Created on Fri May  7 11:52:19 2021

@author: HP
"""

countries=['Kenya', 'Uganda', 'Tanzania', 'South Sudan', 'Rwanda']
for nchi, items in enumerate(countries):
    print(f'{nchi} - {items}')

print("")
for number in range (3,33,10):
    print (number)
    
print("")
for number in range(4):
    print(number)
    
print("")
x=[(1,2),(3,4),(5,6), (7,8),(9,10),(11,12)]
for a,b in x:
    print (a, "plus", b, "equals", a+b)
    
print("")
presidents=["Nkurumah", "Nyerere", "Obote", "Mandela", "Selasie", "Kaunda", "Lumumba"]
i=0
while i<len(presidents):
    print(presidents[i])
    i+=1
    
    
print("")    
for i in range(len(presidents)):
    print("President {}: {}".format(i +1, presidents[i]))
    

print("")
for num, name in enumerate(presidents):
    print("President {}: {}".format(num, name))
    
    
print("")
for i in range(len(countries)):
    print("Country {}: {}".format(i, countries[i]))
    
    


    