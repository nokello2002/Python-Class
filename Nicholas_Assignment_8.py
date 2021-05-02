# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 17:53:02 2021

@author: HP
"""

import json, requests
#the json github url link is for English to Local translation
#We are adding sheng words and meaning in English to the dictionary

data ='https://raw.githubusercontent.com/normansimonr/Dumb-Cogs/master/lolz/data/tranzlashun.json'
resp=requests.get(data)
#print response
print(resp)
#print json content
print(resp.json())

#save the json file in local txt file 
dictionary=resp.json()
with open ('D:\PythonLessons\my_dictionary.txt','w') as file:
    json.dump(dictionary, file)


#open the file and read its contents
print("")
with open ('D:\PythonLessons\my_dictionary.txt','r') as file:
    dictionary={}
    dictionary=json.load(file)
#print dictionary
word=input('Original Word: ')
for value in dictionary.values():
    if word==value:
        print('The translation is: ', dictionary[word])
    
else:
    print('Sorry, that word has no translation in the dictionary')
    #append to the dictionary
    ans=input("Enter sheng meaning: ")
    dictionary[word]=ans
    with open ('D:\PythonLessons\my_dictionary.txt','a') as file:
        json.dump(dictionary, file)


    
    