# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 15:29:56 2021

@author: HP
"""

print("SCHOLARSHIPS MANAGEMENT SYSTEM")
total_score=500

class Scholarship():
    def __init__(self, first_name, last_name, ID_no, address, city, country, region, phone, email, gender, average_score, assignment_grades, zoom_grades):
        self.first_name=first_name
        self.last_name=last_name
        self.ID_no=ID_no
        self.address=address
        self.city=city
        self.country=country
        self.region=region   
        self.phone=phone
        self.email=email
        self.gender=gender
        self.average_score=average_score
        
    def exam_results(self):
        #get quiz and test results
        quiz_1=float(input("Enter results for Quiz 1: "))
        quiz_2=float(input("Enter results for Quiz 2: "))
        quiz_3=float(input("Enter results for Quiz 3: "))
        test_1=float(input("Enter results for Advanced Python: "))
        test_2=float(input("Enter results for Expert Level Python: "))
        
        avg_score=(quiz_1 + quiz_2 + quiz_3 + test_1 + test_2) * 100/total_score
        self.average_score=avg_score
        #print("Student average score in Tests and Quiz: " + str(self.average_score)) 
        
        #get the assignment
        index=1
        ass_total_marks=0
        ass_desc=""
        while index<=10:
            assign_marks=float(input("Enter the marks for #" + str(index) + " assignment: "))
            ass_total_marks += assign_marks
            ass_desc = ass_desc + " " + "Ass #" + str(index) + ": " + str(assign_marks)
            self.assignment_grades =ass_desc
            index=index + 1            
            #print("Student assignment score: " + ass_desc) 
            
        #get the Zoom assignments
        index=1
        zoom_marks=0
        zoom_total_marks=0
        zoom_desc=""
        while index<=3:
            zoom_marks=float(input("Enter the marks for #" + str(index) + " Zoom attendance: "))
            zoom_total_marks=zoom_total_marks + zoom_marks
            zoom_desc=zoom_desc + " " + "Zoom #" + str(index) + ": " + str(zoom_marks)
            self.zoom_grades = zoom_desc 
            index=index + 1
            #print("Student Zoom score: " + zoom_desc) 
        
            
# Create an object student        
student=input("Enter the Student Number: ")
s_fname=input("Enter the First name of the student: ")
s_lname=input("Enter the Last name of student: ")
s_idno=input("Enter the student ID No: ")
s_addr=input("Enter the Address: ")
s_city=input("Enter the City: ")
s_country=input("Enter the Country: ")
flag=False
while flag==False:
    s_region=input("Enter the Region: ")
    s_region=s_region.upper()
    if s_region=='A' or s_region=='O':
        flag=True
    else:
        print("Sorry, region can only be A or O")
        flag=False
    
s_phone=input("Enter the Phone number: ")
s_email=input("Enter the Email address: ")
flag=False
while flag==False:
    s_gender=input("Enter the gender of student(Male/Female): ")
    s_gender=s_gender.title()
    if s_gender=="Male" or s_gender=="Female":
        flag=True
    else:
        print("Sorry, gender can only be Male/Female")
        flag=False
        
s_average_score=0
s_avg_ass_marks=0
s_avg_zoom_marks=0

#Initialize the class
student=Scholarship(s_fname, s_lname, s_idno, s_addr, s_city, s_country, s_region, s_phone, s_email, s_gender, s_average_score, s_avg_ass_marks, s_avg_zoom_marks)        

print("")
student.exam_results()

print("")
print("")
print("")
print("SCHOLARSHIPS MANAGEMENT SYSTEM")
print("Student Report Card")
print("Student Name: " + student.first_name + " " + student.last_name)
print("Student ID No: " + str(student.ID_no))
print("Student Gender: " + student.gender)
print("Student Phone No: " + student.phone)
print("Student Email: " + student.email)
print("Student Address: " + student.address + " " + student.city + " " + student.country)
if s_region=="A":
    print("Student is from Africa")
else:
    print("Student is from diaspora")

print("")
print("Student average score in Tests and Quiz: " + str(student.average_score))  
print("Student assignment score: " + student.assignment_grades) 
print("")
print("Student Zoom score: " + student.zoom_grades) 
  
#Use region and gender to award the scholarship
if s_region=="A":
    if student.average_score >=80 and s_gender=="Male":
        print("Congratulations! You qualify for Full Scholarship")    
    elif student.average_score >=76 and s_gender=="Female":
        print("Congratulations! You qualify for Full Scholarship")      
    else:
        print("Sorry, you are not qualified for a scholarship at the moment")
elif s_region=="O":
    if student.average_score >=80 and s_gender=="Male":
        print("Congratulations! You qualify for Partial Scholarship")    
    elif student.average_score>=76 and s_gender=="Female":
        print("Congratulations! You qualify for Partial Scholarship")      
    else:
        print("Sorry, you are not qualified for a scholarship at the moment")    
else:
    print("Sorry")

    


        
        