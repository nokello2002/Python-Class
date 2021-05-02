# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 17:36:34 2021

@author: HP
"""

#import requests module
import json
import requests
#making a get request
response=requests.get('https://api.github.com')

print(response)
print("")
print(response.json())
