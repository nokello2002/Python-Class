<<<<<<< HEAD
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
            filename="D:\PythonLessons\contacts_json.txt"
            infile=open(filename, "r")
            my_contacts=json.load(infile)
            infile.close()
            #print(my_contacts)
            for key, value in my_contacts.items():
                print("\nRecord ID:", key)
    
                for key in value:
                    print(key + ':', value[key])
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
                filename = "D:\PythonLessons\contacts_json.txt"
                outfile=open(filename, "a+")
                json.dump(my_contacts, outfile)
                outfile.close()
                print("Record saved successfully")
                
                str_action=input("Do you want to create a new contact? (y/n): ")
            else:
                break
                
        elif operation =='3':     #remove/ delete contact
            filename="D:\PythonLessons\contacts_json.txt"
            infile=open(filename, "r+")
            my_contacts={}
            my_contacts=json.load(infile)
            del_str=int(input("Enter Record Number to remove: "))
            ans=input("Are you sure you want to remove this record? (y/n): ")
            if ans=="y":
                #my_contacts[del_str].pop (my_contacts[del_str])
                del my_contacts[del_str]
                print("Record deleted successfully")
            else:
                break
            
        elif operation =='4':     #Update existing dictionary
            filename="D:\PythonLessons\contacts_json.txt"
            outfile=open(filename, "r+")
            my_contacts={}
            my_contacts=json.load(outfile)
            index=int(input("Enter Record Number to Update: "))
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
            if answer=="A":  
                first_name="Enter the First Name to update: "
                my_contacts[index]["First Name"].append(first_name)
            elif answer=="B":
                mid_name=input("Enter middle name to update: ")
                my_contacts[index]["Middle Name"].append(mid_name)
            elif answer=="C":
                last_name=input("Enter last name: ")
                my_contacts[index]["Last Name"].append(last_name)
            elif answer=="D":
                address=input("Enter the mailing address: ")
                my_contacts[index]["Mailing Address"].append(address)
            elif answer=="E":
                city=input("Enter the city: ")
                my_contacts[index]["City"].append(city)
            elif answer=="F":
                country=input("Enter the country: ")
                my_contacts[index]["Country"].append(country)
            elif answer=="G":
                zip_code=input("Enter the Zip Code: ")
                my_contacts[index]["Zip Code"].append(zip_code)
            elif answer=="H":
                email=input("Enter the email address: ")
                my_contacts[index]["Email Address"].append(email)
            elif answer=="I":
                phone=input("Enter the phone number: ")
                my_contacts[index]["Phone Number"].append(phone)
            else:
                print("Wrong input")
            
            json.dump(my_contacts, outfile)
            outfile.close()    
                
        elif operation =='5':     #Search
            filename="D:\PythonLessons\contacts_json.txt"
            infile=open(filename, "r")
            my_contacts={}
            my_contacts=json.load(infile)
            search_string=int(input("Enter Record Number to find: "))
            print(my_contacts[search_string])
            infile.close()
        else:
            break
    
=======
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
            filename="D:\PythonLessons\contacts_json.txt"
            infile=open(filename, "r")
            my_contacts=json.load(infile)
            infile.close()
            #print(my_contacts)
            for key, value in my_contacts.items():
                print("\nRecord ID:", key)
    
                for key in value:
                    print(key + ':', value[key])
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
                filename = "D:\PythonLessons\contacts_json.txt"
                outfile=open(filename, "a+")
                json.dump(my_contacts, outfile)
                outfile.close()
                print("Record saved successfully")
                
                str_action=input("Do you want to create a new contact? (y/n): ")
            else:
                break
                
        elif operation =='3':     #remove/ delete contact
            filename="D:\PythonLessons\contacts_json.txt"
            infile=open(filename, "r+")
            my_contacts={}
            my_contacts=json.load(infile)
            del_str=int(input("Enter Record Number to remove: "))
            ans=input("Are you sure you want to remove this record? (y/n): ")
            if ans=="y":
                #my_contacts[del_str].pop (my_contacts[del_str])
                del my_contacts[del_str]
                print("Record deleted successfully")
            else:
                break
            
        elif operation =='4':     #Update existing dictionary
            filename="D:\PythonLessons\contacts_json.txt"
            outfile=open(filename, "r+")
            my_contacts={}
            my_contacts=json.load(outfile)
            index=int(input("Enter Record Number to Update: "))
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
            if answer=="A":  
                first_name="Enter the First Name to update: "
                my_contacts[index]["First Name"].append(first_name)
            elif answer=="B":
                mid_name=input("Enter middle name to update: ")
                my_contacts[index]["Middle Name"].append(mid_name)
            elif answer=="C":
                last_name=input("Enter last name: ")
                my_contacts[index]["Last Name"].append(last_name)
            elif answer=="D":
                address=input("Enter the mailing address: ")
                my_contacts[index]["Mailing Address"].append(address)
            elif answer=="E":
                city=input("Enter the city: ")
                my_contacts[index]["City"].append(city)
            elif answer=="F":
                country=input("Enter the country: ")
                my_contacts[index]["Country"].append(country)
            elif answer=="G":
                zip_code=input("Enter the Zip Code: ")
                my_contacts[index]["Zip Code"].append(zip_code)
            elif answer=="H":
                email=input("Enter the email address: ")
                my_contacts[index]["Email Address"].append(email)
            elif answer=="I":
                phone=input("Enter the phone number: ")
                my_contacts[index]["Phone Number"].append(phone)
            else:
                print("Wrong input")
            
            json.dump(my_contacts, outfile)
            outfile.close()    
                
        elif operation =='5':     #Search
            filename="D:\PythonLessons\contacts_json.txt"
            infile=open(filename, "r")
            my_contacts={}
            my_contacts=json.load(infile)
            search_string=int(input("Enter Record Number to find: "))
            print(my_contacts[search_string])
            infile.close()
        else:
            break
    
>>>>>>> 46de0a74053b91628abdd774e8fbfac9eeae5889
phone_book()