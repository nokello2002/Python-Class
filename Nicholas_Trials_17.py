# -*- coding: utf-8 -*-
"""
Created on Sat May 15 10:23:15 2021

@author: HP
"""

from faker import Faker

fake=Faker()
first=(fake.first_name())
last=(fake.last_name())
full_name = first + " " + last
print(full_name)
print(fake.phone_number())
print(fake.city())
print(fake.state())
print(fake.zipcode())
print(fake.country())