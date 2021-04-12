# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 18:32:53 2021

@author: HP
"""

#Enter the price of the House you wish to Buy
print("Enter the house price")
price = input("Enter the house price: ")

#Enter the first name
print("Enter the first name")
first_name = input("Enter the first name: ")

#Enter the last name
print("Enter the last name")
last_name = input("Enter the last name: ")

fullname = first_name + " " + last_name

#Enter the email
print("Enter the email address")
email = input("Enter the email address: ")

#Enter the phone number
print("Enter the phone number")
phone = input("Enter the phone number: ")

#Enter the mailing
print("Enter the mailing address")
address=input("Enter the mailing address: ")

#Enter the mailing
print("Enter the City")
city = input("Enter the City: ")

#Enter the mailing
print("Enter the zip code")
zipcode = input("Enter the zip code: ")

CreditScore=679
#Qualify for loans with the best interest rates
if 780<= CreditScore <=850:
    credit_status=("Excellent Credit")
    print("Zero Down Payment")
    downPayment = 0.10 * float(price)

#Usually qualify for loans with the best interest rates
elif 740 <=CreditScore <=779:
    credit_status=("Very Good")
    downPayment = 0.1 * float(price)

#May face slightly higher loan Interest rates
elif 720<= CreditScore <= 739:
    credit_status=("Above Average")
    downPayment = 0.3 * float(price)

#May qualify for most loans of higher interest rates
elif 680<= CreditScore <= 719:
    credit_status=("Average")
    downPayment = 0.6 * float(price)

#May qualify for most loans at significant higher Interest rates
elif 620<= CreditScore <= 679:
    credit_status=("Below Average")
    downPayment = 0.18 * float(price)

#Usually has some credit issues; will probably not qualify for most loans
elif 580<= CreditScore <= 619:
    credit_status=("Poor Credit Score")
    downPayment = 0.20 * float(price)

#Facing extreme credit issue
else: 
    CreditScore < 520
    credit_status=("Poor Credit Score")
    downPayment = 0.25 * float(price)

print ("Full name:" + fullname)
print ("Phone Number: " + phone)
print ("Email address: " + email)
print ("Physical Address: " + address)
print ("City: " + city  + "Zipcode:"  + zipcode)
print ("New house price: " + str(price))
print ("Credit Score: " + str(CreditScore))
print ("Credit Status: " + credit_status)
print ("CONGRATULATIONS - YOU NOW OWN YOUR DREAM HOME")