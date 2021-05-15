# -*- coding: utf-8 -*-
"""
Created on Sat May 15 10:01:36 2021

@author: HP
"""
import csv
from faker import Faker

record_count=100
fake=Faker()

with open ('Employee_Records.csv', 'w', newline= '') as csvfile:
    fieldnames=['First_Name', 'Last_Name', 'SSN', 'Email_Address', 'Phone', 'Address', 'City', 'State', 'Zipcode', 'Country']
    writer=csv.DictWriter(csvfile, fieldnames= fieldnames)
    writer.writeheader()
    
    for i in range (record_count):
        writer.writerow({'First_Name':fake.first_name(), 'Last_Name':fake.last_name(), 'SSN': fake.ssn(),
                         'Email_Address': fake.email(), 'Phone': fake.phone_number(), 'Address': fake.street_address(),
                         'City': fake.city(), 'State': fake.state(), 'Zipcode': fake.zipcode(), 'Country': fake.country()})
        
    
    print("Records saved successfully")