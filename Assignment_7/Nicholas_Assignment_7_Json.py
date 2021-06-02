
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 17:22:04 2021

@author: HP
"""

print("Motorola Phone Book")
print("")
import json
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
            try:
                my_contacts={}
                filename="D:\PythonLessons\Assignment_7\contacts.json"
                infile=open(filename, "r")
                my_contacts=json.load(infile)
                if len(my_contacts)==0:
                    print("No records to view")
                else:                      
                    #my_contacts=json.load(infile)
                    infile.close()
                    for key, value in my_contacts.items():
                        print("\nRecord ID:", key)
    
                        for key in value:
                            print(key + ':', value[key])
            except FileNotFoundError: 
                msg = "Can’t find {0}.".format(filename) 
                print(msg)
                my_contacts={}                
            
        elif operation =='2':     #add contact
            index=0
            str_action="y"
            
            try:
                filename="D:\PythonLessons\Assignment_7\contacts.json"
                infile=open(filename, "r")
                if infile.seek==0:
                    phone_contact={}    
                else:
                    phone_contact=json.load(infile)
                    infile.close()
            except IOError:
                phone_contact={}    
            
            while str_action=="y":
                my_contacts={}
                #The dictionary will have the design below
                #my_contacts={index:{"First Name":[], "Middle Name":[], "Last Name":[], "Mailing Address":[], "City":[], 
                #                    "Country":[], "Zip Code":[], "Email Address":[], "Phone Number":[]}}
                #prompt for the contacts to be entered
                index=int(input("Enter Record Number: "))
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
                my_contacts["First Name"]=(first_name)
                my_contacts["Middle Name"]=(mid_name)
                my_contacts["Last Name"]=(last_name)
                my_contacts["Mailing Address"]=(address)
                my_contacts["City"]=(city)
                my_contacts["Country"]=(country)
                my_contacts["Zip Code"]=(zip_code)
                my_contacts["Email Address"]=(email)
                my_contacts["Phone Number"]=(phone)
                
                phone_contact[index]=my_contacts
                print("Customer Details")
                print(my_contacts)
                #Open the Contacts file to save details of phone book
                filename = "D:\PythonLessons\Assignment_7\contacts.json"
                outfile=open(filename, "w")
                json.dump(phone_contact, outfile)
                outfile.close()
                print("Record saved successfully")
                
                str_action=input("Do you want to create a new contact? (y/n): ")
                
        elif operation =='3':     #remove/ delete contact
            try:
                filename="D:\PythonLessons\Assignment_7\contacts.json"
                infile=open(filename, "r+")
                my_contacts={}
                my_contacts=json.load(infile)
                del_str=input("Enter Record Number to remove: ")
                ans=input("Are you sure you want to remove this record? (y/n): ")
                if ans=="y":
                    if del_str in my_contacts.keys():
                        del my_contacts[del_str]
                        #print(my_contacts)
                        with open("D:\PythonLessons\contacts.json", "w") as file:
                            json.dump(my_contacts, file) 
                            print("Record deleted successfully")
            except IOError:
                print("Error in program")
            
        elif operation =='4':     #Update existing dictionary
            filename="D:\PythonLessons\Assignment_7\contacts.json"
            outfile=open(filename, "r")
            my_contacts={}
            my_contacts=json.load(outfile)
            index=input("Enter Record Number to Update: ")
            answer= input('''
            Select item to update:
                [A] First Name
                [B] Middle Name
                [C] Last Name
                [D] Mailing Address
                [E] City
                [F] Country
                [G] Zip Code
                [H] Email Address
                [I] Telephone Number
                         ''')
            answer=answer.upper()
            for w in my_contacts.keys():
                if str(index) in w:   # search the customer contact from the database
                    if answer=="A":  
                        first_name=input("Enter the First Name to update: ")
                        my_contacts[index]["First Name"]=(first_name)
                    elif answer=="B":
                        mid_name=input("Enter middle name to update: ")
                        my_contacts[index]["Middle Name"]=(mid_name)
                    elif answer=="C":
                        last_name=input("Enter last name: ")
                        my_contacts[index]["Last Name"]=(last_name)
                    elif answer=="D":
                        address=input("Enter the mailing address: ")
                        my_contacts[index]["Mailing Address"]=(address)
                    elif answer=="E":
                        city=input("Enter the city: ")
                        my_contacts[index]["City"]=(city)
                    elif answer=="F":
                        country=input("Enter the country: ")
                        my_contacts[index]["Country"]=(country)
                    elif answer=="G":
                        zip_code=input("Enter the Zip Code: ")
                        my_contacts[index]["Zip Code"]=(zip_code)
                    elif answer=="H":
                        email=input("Enter the email address: ")
                        my_contacts[index]["Email Address"]=(email)
                    elif answer=="I":
                        phone=input("Enter the phone number: ")
                        my_contacts[index]["Phone Number"]=(phone)
                    else:
                        print("Wrong input")
                    #print(my_contacts)
                    with open("D:\PythonLessons\Assignment_7\contacts.json", "w") as file:
                        json.dump(my_contacts, file) 
                        print("Record Updated Successfully")
                
        elif operation =='5':     #Search
            filename="D:\PythonLessons\Assignment_7\contacts.json"
            infile=open(filename, "r")
            my_contacts={}
            my_contacts=json.load(infile)
            search_string=input("Enter Record Number to find: ")
            for w in my_contacts.keys():
                if str(search_string) in w:   # search the customer contact from the database
                    print(my_contacts[search_string])
            infile.close()
        else:
            break

phone_book()