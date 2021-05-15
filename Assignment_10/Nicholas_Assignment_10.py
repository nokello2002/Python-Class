# -*- coding: utf-8 -*-
"""
Created on Sat May 15 12:14:07 2021

@author: HP
"""
#Program demostrating use of CSV, Faker and pandas modules
#Program to download data using the Faker module
#Save the data to csv file, 100 rows in total
#Transfer the csv data to mysql database

import csv
from faker import Faker
import pandas
import mysql.connector as mysql
from mysql.connector import Error

#Step 0: To avoid confusion when veryfing csv verses the mysql data truncate the table
connection=mysql.connect(host='localhost', database='employee_data', user='root', password='Th@nkuL0rd')
#To ensure that you have fresh records in the database, just truncate the table
sql="TRUNCATE TABLE employees"
cursor=connection.cursor()
cursor.execute (sql)

#Step 1: Write data from Faker module into CSV
record_count=100
fake=Faker()

with open ('D:\PythonLessons\Assignment_10\Employee_Records.csv', 'w', newline= '') as csvfile:
    fieldnames=['First_Name', 'Last_Name', 'SSN', 'Email_Address', 'Phone', 'Address', 'City', 'State', 'Zipcode', 'Country']
    writer=csv.DictWriter(csvfile, fieldnames= fieldnames)
    writer.writeheader()
    
    for i in range (record_count):
        writer.writerow({'First_Name':fake.first_name(), 'Last_Name':fake.last_name(), 'SSN': fake.ssn(),
                         'Email_Address': fake.email(), 'Phone': fake.phone_number(), 'Address': fake.street_address(),
                         'City': fake.city(), 'State': fake.state(), 'Zipcode': fake.zipcode(), 'Country': fake.country()})
        
    
    print("Records saved successfully")

#Step 2: Read data from CSV file using the pandas module
print("")
empdata= pandas.read_csv('D:\PythonLessons\Assignment_10\Employee_Records.csv')
print(empdata)

#Step 3: Push the data to MySQL from pandas
try:
    #establish connection to the database
    connection=mysql.connect(host='localhost', database='employee_data', user='root', password='Th@nkuL0rd')
    if connection.is_connected():
        cursor=connection.cursor()
        cursor.execute("Select database();")
        record=cursor.fetchone()
        print("You are connected to database: ", record)
        
    #pick the data in the pandas handle and insert to the table in mysql
    #loop through the data frame 
    print("")
    print("Converting the CSV to MySQL using Pandas module")
    for i, row in empdata.iterrows():
        sql="INSERT INTO employees VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, tuple(row))
    print("Records Saved")
    connection.commit()
    
    
except Error as e:
    print("Error while connecting to the database", e)
    


#Step 4: Read the data from MySQL to confirm it is same as data from cSV
print("")
print("")
print("Displaying the MySQL Data retrieved")

#insert the new records
sql="SELECT * FROM employees"
cursor.execute(sql)
#fetch all the records
result=cursor.fetchall()
for i in result:
    print(i)
    
cursor.close()
connection.close()
