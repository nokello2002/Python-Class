# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 17:32:57 2021

@author: HP
"""

def CSA_Converter():
    mylist = []
    while True:
        operation = input('''
Select Option:
[1] Temperature from Fahrenheit to Celsius and back
[2] Convert Nautical Miles to KMS and back
[3] Convert Kilometer to Miles and back
[4] Convert Centimeters to meters and back
[5] Convert Yard to Meters and back
[6] Convert Inches to Centimeters and back
[7] Exit programm

''')
        if operation == '1':
            temp=float(input("Enter the temperature in Fahrenheit: "))
            celcius=(temp -32) * 5/9
            print("Farenheight: ", + temp)
            print("Celcius: ", + round(celcius,2))
        elif operation == '2':
            nautic_mile=float(input("Enter the Distance in nautical miles: "))
            kms=1.852 * nautic_mile
            print("Nautical Miles: ", + nautic_mile)
            print("kilometers: ", + round(kms,2)) 
        elif operation == '3':
            km=float(input("Enter the Distance in kilometers: "))
            miles=0.621371 * km
            print("Kilometers: ", + km)
            print("Miles: ", + round(miles,2))
        elif operation == '4':
            cents=float(input("Enter the Distance in centimeters: "))
            meter=0.01 * cents
            print("Centimeters: ", + cents)
            print("Meters: ", + round(meter,2))
        elif operation == '5':
            yard=float(input("Enter the Distance in yards: "))
            mtr=0.9144 * yard
            print("Yard: ", + yard)
            print("Meters: ", + round(mtr,2))
        elif operation == '6':
            inch=float(input("Enter the Distance in inches: "))
            cms=2.54 * inch
            print("Inches: ", + inch)
            print("Centimetres: ", + round(cms,2)) 
        elif operation == '7':
            break

        else:
            print("Invalid choice. Please try again.")

CSA_Converter()