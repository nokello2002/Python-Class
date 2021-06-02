# -*- coding: utf-8 -*-
"""
Created on Wed May 12 10:13:38 2021

@author: HP
"""
import json
import io
import mysql.connector
#connect to MySQL database 

print("Kenya Power & Lightning Company")
print("Welcome")

#check for the database connection
from mysql.connector import Error
try:
    connection=mysql.connector.connect(host='localhost', database='electricity', user='root', password='Th@nkuL0rd')
    if connection.is_connected():
        db_info=connection.get_server_info()
        print("Connected to MySQL Server Version: " + db_info)
        cursor=connection.cursor()
        cursor.execute("Select database();")
        record=cursor.fetchone()
        print("You are connected to database", record)
        
except Error as e:
    print("Error when connecting to the database ", e)
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        
    
#main program starts here
while True:
    operation= input('''
        Select Options:
            [1] Add Customers
            [2] Display Electricity Charges
            [3] Bill Customers
            [4] Print Bills
            [5] List Customers
            [6] Quit
                         ''')
    if operation =='1':     #adding new customers
        #check if the customer file exists and load the details in the customer dictionary
        try:
            with open ("D:\PythonLessons\Assignment_9\customer.txt", "r") as file:
                main_customer={}
                main_customer=json.load(file)
                #print(main_customer)
        except IOError:
            main_customer={}
        
        str_action="y"
        custid=1        #initialize the variable
        while str_action=="y":
            customer={}
            #customer={custid:{"First Name":[], "Middle Name":[], "Last Name":[], "Mailing Address":[], "City":[], 
            #                        "Country":[], "Zip Code":[], "Email Address":[], "Phone Number":[],
            #                        "Zone": [], "Zone Category": []}}
            #prompt for the customer details to be entered
            custid=int(input("Enter Customer Number: "))
            first_name=input("Enter first name: ")
            mid_name=input("Enter middle name: ")
            last_name=input("Enter last name: ")
            address=input("Enter the mailing address: ")
            city=input("Enter the city: ")
            country=input("Enter the country: ")
            zip_code=input("Enter the Zip Code: ")
            email=input("Enter the email address: ")
            phone=input("Enter the phone number: ")
            zone=str.upper(input("Enter the Zone (R for Rural Area or U for Urban Area): "))
            zone_category=str.upper(input("Enter the Zone category (R for Residential, L for Light Industries, H for Heavy Industrial): "))
                
            #attach the values to respective keys in the customer dictionary
            customer["First Name"]=(first_name)
            customer["Middle Name"]=(mid_name)
            customer["Last Name"]=(last_name)
            customer["Mailing Address"]=(address)
            customer["City"]=(city)
            customer["Country"]=(country)
            customer["Zip Code"]=(zip_code)
            customer["Email Address"]=(email)
            customer["Phone Number"]=(phone)
            customer["Zone"]=(zone)
            customer["Zone Category"]=(zone_category)
            
            #create main customer based customer Id
            main_customer[custid]=customer
            
            #print(customer[custid])
            #Open the Contacts text file to save details of phone book
            with open ("D:\PythonLessons\Assignment_9\customer.txt", "w") as file:
                json.dump(main_customer,file)
                
            #save to MySQL table
            #establishing the connection
            connection=mysql.connector.connect(host='localhost', database='electricity', user='root', password='Th@nkuL0rd')
            #Creating a cursor object using the cursor() method
            cursor=connection.cursor()

            # Preparing SQL query to INSERT a record into the database.
            cursor.execute('insert into customers values ("%d","%s","%s", "%s","%s", "%s","%s", "%s","%s", "%s","%s", "%s")' % (custid, first_name, mid_name, last_name, address, city, country, zip_code, email, phone, zone, zone_category))
            connection.commit()
            
            # Closing the connection
            connection.close()
            
            print("Record saved successfully")
                
            str_action=input("Do you want to create a new customer? (y/n): ")
    elif operation =='2':
        print("1 Kilowatt of electricity is Kshs 10.00 in Rural Area (Residential)")
        print("1 Kilowatt of electricity is Kshs 15.00 in Urban Area (Residential)")
        print("1 Kilowatt of electricity is Kshs 20.00 in Urban Area (Light Industrial)")
        print("1 Kilowatt of electricity is Kshs 23.00 in Rural Area (Light Industrial)")
        print("1 Kilowatt of electricity is Kshs 27.00 in Rural Area (Heavy Industrial)")
        print("1 Kilowatt of electricity is Kshs 10.00 in Urban Area (Heavy Industrial)")
        
    elif operation =='3':     #Bill customers
        filename="D:\PythonLessons\Assignment_9\customer.txt"
        infile=open(filename, "r")
        customer={}
        customer=json.load(infile)
        search_string=input("Enter Customer Number to bill: ")
        for w in customer.keys():
            if str(search_string) in w:   # search the customer from the database
                print("Customer No: {} Customer Name: {} {}".format(search_string, customer[search_string]["First Name"], customer[search_string]["Last Name"]))
                month=int(input("Enter the Billing Month: "))
                year=int(input("Enter the Billing Year: "))
                consumption=float(input("Enter the amount of electricity consumed: "))
                    
                #initialize nominal tax
                city_tax=4/100
                    
                #determine amount of discount to give
                if consumption >=200 and consumption<= 450:
                    discount=0.03
                elif consumption >=451 and consumption<= 500:
                    discount=0.05
                elif consumption >=501 and consumption<= 601:
                    discount=0.07
                elif consumption >=602 and consumption<= 701:
                    discount=0.09
                elif consumption >=702 and consumption<= 801:
                    discount=0.11
                elif consumption >=802:
                    discount=0.12
                else:
                    discount=0
                        
                        
                #calculate the cost depending on prevailing rates per zone and zone classification
                if customer[search_string]["Zone"]=="R":
                    strzone="Rural"
                    if customer[search_string]["Zone Category"]=="R":
                        unit_cost=10
                        state_vat=0.10
                        strcategory="Residential"
                    elif customer[search_string]["Zone Category"]=="L":
                        unit_cost=23
                        state_vat=0.15
                        strcategory="Light Industry"
                    elif customer[search_string]["Zone Category"]=="H":
                        unit_cost=27
                        state_vat=0.15
                        strcategory="Heavy Industry"
                    else:
                        break
                elif customer[search_string]["Zone"]=="U":
                    strzone="Urban"
                    if customer[search_string]["Zone Category"]=="R":
                        unit_cost=15
                        state_vat=0.10
                        strcategory="Residential"
                    elif customer[search_string]["Zone Category"]=="L":
                        unit_cost=20
                        state_vat=0.15
                        strcategory="Light Industry"
                    elif customer[search_string]["Zone Category"]=="H":
                        unit_cost=30
                        state_vat=0.15
                        strcategory="Heavy Industry"
                    else:
                        break
                else:
                    break
                    
                if discount==0:
                    calculated_rate = (consumption * unit_cost)
                    disc=0
                    discounted_electricity=calculated_rate
                    state_vated_amt=discounted_electricity * state_vat
                    nominal_tax= discounted_electricity * city_tax
                    final_cost=discounted_electricity + state_vated_amt + nominal_tax
                else:
                    calculated_rate = (consumption * unit_cost)
                    disc=(consumption * unit_cost * discount)
                    discounted_electricity= calculated_rate - disc
                    state_vated_amt=discounted_electricity * state_vat
                    nominal_tax= discounted_electricity * city_tax
                    final_cost=discounted_electricity + state_vated_amt + nominal_tax
                   
                print("")
                #Display the customer slip
                cstr= "Kenya Power"
                print(cstr.center(45, '#'))
                print("Month: {} Year {}".format(month, year))
                print("")
                print("Customer No: {} Customer Name: {} {}".format(search_string, customer[search_string]["First Name"], customer[search_string]["Last Name"]))
                print("Customer Zone: {} - {}".format(strzone, strcategory))
                print("")
                print("Units (kwh):  %5.2f" % (consumption))
                print("Amount: %5.2f" % (calculated_rate))
                print("Discount: %5.2f" % disc)
                print("Discounted Amount: %5.2f" % discounted_electricity)
                print("State Vat: %5.2f" % state_vated_amt)
                print("Nominal Vat: %5.2f" % nominal_tax)
                print("Total Cost: %5.2f" % final_cost)
                print("")
                print("Thank you for being our valued customer")
                cstr="End of Legal Receipt"
                print(cstr.center(45, '#'))
                
                #save to MySQL table
                #establishing the connection
                connection=mysql.connector.connect(host='localhost', database='electricity', user='root', password='Th@nkuL0rd')
                #Creating a cursor object using the cursor() method
                cursor=connection.cursor()
                
                #determine if same customer had been billed same month and year and delete current record
                sqlstr="DELETE FROM customer_billing WHERE CustomerID = %d AND Billing_month= %d and Billing_Year = %d" % (int(search_string), month, year)
                cursor.execute (sqlstr)

                # Preparing SQL query to INSERT a record into the database.
                cursor.execute('insert into customer_billing values ("%d","%d","%d", "%f","%f", "%f","%f", "%f","%f", "%f","%f", "%f")' % (month, year, int(search_string), consumption, unit_cost, calculated_rate, discount, disc, discounted_electricity, state_vated_amt, nominal_tax, final_cost))
                connection.commit()
            
                # Closing the connection
                connection.close()
                    
        infile.close()
    elif operation == '4':
        search_string=input("Enter Customer Number to bill: ")
        #establishing the connection
        connection=mysql.connector.connect(host='localhost', database='electricity', user='root', password='Th@nkuL0rd')
        #Creating a cursor object using the cursor() method
        cursor=connection.cursor(dictionary=True)
                
        #Search for customer ID in the table. If found proceed or else show no such customer
        sqlstr="SELECT CustomerID, FirstName, LastName, Zone, ZoneCategory FROM customers WHERE CustomerID = %s"  % (int(search_string))
        cursor.execute (sqlstr)
        record= cursor.fetchall()

        if cursor.rowcount >0:
            for row in record:
            #assign values to variables
                custid=row['CustomerID']
                first_name=row['FirstName']
                last_name=row['LastName']
                strzone=row['Zone']
                strcategory=row['ZoneCategory']
                
                if strzone=="R":
                    strzone="Rural"
                elif strzone=="U":
                    strzone="Urban"
                else:
                    strzone=""
                
                if strcategory=='R':
                    strcategory="Residential"
                if strcategory=='L':
                    strcategory="Light Industry"    
                else: 
                    strcategory=='Heavy Industry'
                
                
                print("Customer No: {} Customer Name: {} {}".format(custid, first_name, last_name))
                month=int(input("Enter the Billing Month: "))
                year=int(input("Enter the Billing Year: "))
            
                #search for billing information
                sqlstr="SELECT * FROM customer_billing WHERE CustomerID = %d AND Billing_month= %d and Billing_Year = %d" % (int(search_string), month, year)
                cursor.execute (sqlstr)
                result=cursor.fetchall()
                #If billing for that month is found print receipt else show no billing info
                if cursor.rowcount >0:
                    for i in result:
                        consumption=i['Units_Utilized']
                        calculated_rate=i['Item_Price']
                        disc=i['Discount']
                        discounted_electricity=i['Discounted_Amount']
                        state_vated_amt=i['State_VAT']
                        nominal_tax=i['Nominal_VAT']
                        final_cost=i['Total_Cost']
                        
                        print("")
                        #Display the customer slip
                        cstr= "Kenya Power"
                        print(cstr.center(45, '#'))
                        print("Month: {} Year {}".format(month, year))
                        print("")
                        print("Customer No: {} Customer Name: {} {}".format(custid, first_name, last_name))
                        print("Customer Zone: {} - {}".format(strzone, strcategory))
                        print("")
                        print("Units (kwh):  %5.2f" % (consumption))
                        print("Amount: %5.2f" % (calculated_rate))
                        print("Discount: %5.2f" % disc)
                        print("Discounted Amount: %5.2f" % discounted_electricity)
                        print("State Vat: %5.2f" % state_vated_amt)
                        print("Nominal Vat: %5.2f" % nominal_tax)
                        print("Total Cost: %5.2f" % final_cost)
                        print("")
                        print("Thank you for being our valued customer")
                        cstr="End of Legal Receipt"
                        print(cstr.center(45, '#'))
                    
                else:
                    print("No billing information is available for the selected month and year")
                
        else:
            print("No such customer exist in our system")
        
    
    elif operation =='5':       #List customers
            filename="D:\PythonLessons\Assignment_9\customer.txt"
            infile=open(filename, "r")
            main_customer=json.load(infile)
            infile.close()
            #print(my_contacts)
            for key, value in main_customer.items():
                print("\nRecord ID:", key)
    
                for key in value:
                    print(key + ':', value[key])
    
    if operation =='6':     #quit
        break