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

#create object dictionary and add the json data 
dictionary={}
dictionary=resp.json()

while True:
    operation= input('''
        Select Options:
            [1] Save Original Dictionary from Net
            [2] List Words and their Translation locally
            [3] Add New Word and Translation locally
            [4] Remove Word and Translation locally
            [5] Search Local Dictionary
            [6] Quit
                         ''')
    if operation =='1':       #save dictionary
        with open ('D:\PythonLessons\Assignment_8\my_dictionary.txt','w') as file:
            json.dump(dictionary, file)
            print("Dictionary saved successfully to location specified")

    elif operation=='2':
        #open the file and read its contents
        print("")
        with open ('D:\PythonLessons\Assignment_8\my_dictionary.txt','r') as file:
            dictionary={}
            dictionary=json.load(file)
            #print dictionary
            print(dictionary)
            
    elif operation=='3':
        print("")
        with open ('D:\PythonLessons\Assignment_8\my_dictionary.txt','r') as file:
            dictionary={}
            dictionary=json.load(file)
            word=input('Enter Original Word to search for: ')
            for w in dictionary.keys():
                if word == w:
                    print(word + ' has translation as ', dictionary[w])
    
            if word not in dictionary:
                #append to the dictionary
                ans=input("Enter sheng meaning: ")
                dictionary[word] = ans
                with open ('D:\PythonLessons\Assignment_8\my_dictionary.txt','w') as file:
                    json.dump(dictionary, file)
    elif operation=='4':
        print("")
        with open ('D:\PythonLessons\Assignment_8\my_dictionary.txt','r') as file:
            dictionary={}
            dictionary=json.load(file)
            word=input('Enter Original Word to delete: ')
            if "word" in dictionary:
                del dictionary[word]
                with open ('D:\PythonLessons\Assignment_8\my_dictionary.txt','w') as file:
                    json.dump(dictionary, file)
                    print("Record deleted successfully")
            else:
                print("The entered word is not available to be deleted")
    elif operation=='5':
        print("")
        with open ('D:\PythonLessons\Assignment_8\my_dictionary.txt','r') as file:
            dictionary={}
            dictionary=json.load(file)
            word=input('Enter Original Word to search for: ')
            
            if "word" in dictionary:
                print(word + ' has translation as ', dictionary[word]) #display value
    
            else:
                print('Sorry, that word has no translation in the dictionary')
                
    else:
        break
                

