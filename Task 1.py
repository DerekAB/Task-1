#Name:                  AreaCalc.py
#Author:                Derek Baker
#Date Created:          02-02-2023
#Date Last Modified:    02-02-2023
#
#Purpose:
#
#The purpose of this program is to ask the user if they want to calculate the area of a circle, rectangle, or triangle.

answer = input("Please enter if you would like to calculate the area of a triangle, circle, or rectangle. Or if you would like to exit: ") #Get the user's choice 

while answer.strip().upper() == "TRIANGLE":
    triangleLength = float(input("Please enter the length of triangle in centimetres: "))
    
    triangleArea = (triangleLength * triangleLength) / 2
    trianglePerimeter = triangleLength * 3
    
    print("The area of the triangle is: " + str(triangleArea) + "cm^2")
    
    break
    
while answer.strip().upper() == "RECTANGLE":
    print(";asdf")
    
while answer.strip().upper() == "CIRCLE":
    print("a;slkdfj")