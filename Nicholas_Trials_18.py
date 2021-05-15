# -*- coding: utf-8 -*-
"""
Created on Sat May 15 11:08:32 2021

@author: HP
"""
#program to demostrate use of csv files
import csv

#Reading data from csv file method 1
#Reading CSV Files With csv
with open('D:\PythonLessons\employee_birthday.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')
    

#Reading data from csv file method 2
#Reading CSV Files Into a Dictionary With csv
print("")
with open('D:\PythonLessons\employee_birthday.txt', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        print(f'\t{row["name"]} works in the {row["department"]} department, and was born in {row["birthday month"]}.')
        line_count += 1
    print(f'Processed {line_count} lines.')
    

#writing data to a csv file method 1
#Writing CSV Files With csv 
print("")
with open('D:\PythonLessons\employee_file.csv', mode='w') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    employee_writer.writerow(['John Smith', 'Accounting', 'November'])
    employee_writer.writerow(['Erica Meyers', 'IT', 'March'])
    
    print("Records saved successfully")
    

#writing data to a csv file method 2
#Writing CSV File From a Dictionary With csv
print("")
with open('D:\PythonLessons\employee_file2.csv', mode='w') as csv_file:
    fieldnames = ['emp_name', 'dept', 'birth_month']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'emp_name': 'John Smith', 'dept': 'Accounting', 'birth_month': 'November'})
    writer.writerow({'emp_name': 'Erica Meyers', 'dept': 'IT', 'birth_month': 'March'})
    
    print("Records saved successfully")
    
    

#Reading CSV Files With pandas
print("")
import pandas
df = pandas.read_csv('hrdata.txt', parse_dates=['Hire Date'])
print(df)

#Writing CSV Files With pandas
print("")
df = pandas.read_csv('hrdata.txt', 
            index_col='Employee', 
            parse_dates=['Hired'],
            header=0, 
            names=['Employee', 'Hired', 'Salary', 'Sick Days'])
df.to_csv('hrdata_modified.txt')
print("Records saved successfully")