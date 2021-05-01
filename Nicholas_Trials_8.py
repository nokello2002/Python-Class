# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 16:56:19 2021

@author: HP
"""

#Writing JSON to a file
import json
#saving data to json file
data={}
data['Student']=[]
data['Student'].append({
    'name': 'Hellen Koech',
    'website': 'opensourceIT2020.com',
    'from': 'Vihiga'})
data['Student'].append({
    'name': 'Faith Moraa',
    'website': 'google.com',
    'from': 'Mombasa'})
data['Student'].append({
    'name': 'Grace Ngima',
    'website': 'apple.com',
    'from': 'Nyeri'})

with open ('D:\PythonLessons\Students.txt', 'w') as outfile:
    json.dump(data, outfile)


#retrieving data from json file    
with open ('D:\PythonLessons\Students.txt', 'r') as infile:
    data=json.load(infile)
    for p in data["Student"]:
        print('Name: ' + p['name'])
        print('Website: ' + p['website'])
        print('From: ' + p['from'])
        print("")
        
        
    