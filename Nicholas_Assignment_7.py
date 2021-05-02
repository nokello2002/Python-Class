# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 09:21:51 2021

@author: HP
"""

print("Motorola Phone Book")
print("")

def phone_book():
    #phone_menu=[]
    while True:
        operation= input('''
            Select Options:
                [1] List Phone Numbers
                [2] Add Contact
                [3] Remove Contact
                [4] Update Contact
                [5] Lookup Contact by Number
                [6] Quit
                         ''')
        if operation =='1':       #List contacts
            with open ("D:\PythonLessons\contacts.txt", "r") as file:
                print(file.read())
                
        elif operation =='2':     #add contact
            index=0
            str_action="y"
            my_contacts={}
            
            while str_action=="y":
                index+=1
                #Create an empty dictionary to hold phone details
                my_contacts={index:{"First Name":[], "Middle Name":[], "Last Name":[], "Mailing Address":[], "City":[], 
                                    "Country":[], "Zip Code":[], "Email Address":[], "Phone Number":[]}}
                #prompt for the contacts to be entered
                first_name=input("Enter first name: ")
                mid_name=input("Enter middle name: ")
                last_name=input("Enter last name: ")
                address=input("Enter the mailing address: ")
                city=input("Enter the city: ")
                country=input("Enter the country: ")
                zip_code=input("Enter the Zip Code: ")
                email=input("Enter the email address: ")
                phone=input("Enter the phone number: ")
                
                #attach the values to respective keys in the contacts dictionary
                my_contacts[index]["First Name"].append(first_name)
                my_contacts[index]["Middle Name"].append(mid_name)
                my_contacts[index]["Last Name"].append(last_name)
                my_contacts[index]["Mailing Address"].append(address)
                my_contacts[index]["City"].append(city)
                my_contacts[index]["Country"].append(country)
                my_contacts[index]["Zip Code"].append(zip_code)
                my_contacts[index]["Email Address"].append(email)
                my_contacts[index]["Phone Number"].append(phone)
                
                print(my_contacts)
                #Open the Contacts file to save details of phone book
                with open ("D:\PythonLessons\contacts.txt", "a") as file:
                    for key, value in my_contacts.items():
                        file.write('%s:%s\n' % (key, value))
                        print("Record saved successfully")
                
                str_action=input("Do you want to create a new contact? (y/n): ")
            else:
                break
                
        elif operation =='3':     #remove contact
            with open ("D:\PythonLessons\contacts.txt", "r") as file:
                my_contacts={}
                my_contacts=file.read()
                del_str=int(input("Enter Record Number to remove: "))
                print(my_contacts)
                #print(my_contacts[del_str])
                #"my_contacts.pop (my_contacts[del_str])
            
        elif operation =='4':     #Update existing dictionary
            with open ("D:\PythonLessons\contacts.txt", "r") as file: 
                my_contacts=file.read()
                search_string=int(input("Enter Record Number to Update: "))
                for strx in my_contacts[search_string]:
                    if strx ==search_string:
                        print(my_contacts[index])
                        
                
                
        elif operation =='5':     #Search
            with open ("D:\PythonLessons\contacts.txt", "r") as file:
                my_contacts={}
                my_contacts=file.read()
                search_string=int(input("Enter Record Number to find: "))
                print(my_contacts)
                
        else:
            break
    
phone_book()

        