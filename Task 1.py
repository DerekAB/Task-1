#Name:                  AreaCalc.py
#Author:                Derek Baker
#Date Created:          02-02-2023
#Date Last Modified:    02-02-2023
#
#Purpose:
#
#The purpose of this program is to ask the user if they want to calculate the area of a circle, rectangle, or triangle.
import math
answer = input("Please enter if you would like to calculate the area of a triangle, " + \
               "circle, or rectangle. Or if you would like to exit: ") #Get the user's choice 

if answer.strip().upper() == "TRIANGLE":
    triangleLength = float(input("Please enter the length of triangle in centimetres: "))
    
    triangleArea = (triangleLength * triangleLength) / 2
    trianglePerimeter = triangleLength * 3
    
    print("The area of the triangle is: " + str(triangleArea) + "cm^2.")
    print("The perimeter of the triangle is " + str(trianglePerimeter) + "cm.")
    
if answer.strip().upper() == "RECTANGLE":
    rectangleLength = float(input("Please enter the length of the rectangle: "))
    
    rectangleArea = rectangleLength * 2 
    rectanglePerimeter = rectangleLength * 4 
    
    print("The area of the rectangle is " + str(rectangleArea) + "cm^2.")
    print("The perimeter of the rectangle is " + str(rectanglePerimeter) + "cm.")
    
if answer.strip().upper() == "CIRCLE":
    circleRadius = float(input("Please enter the radius of the circle: "))
    
    circleArea = math.pi * (circleRadius * circleRadius)
    circlePerimeter = 2 * math.pi * circleRadius
    
    print("The area of the circle is " + str(circleArea) + "cm^2.")
    print("The perimeter of the circle is " + str(circlePerimeter) + "cm.")
    
if answer.strip().upper() == "EXIT":
    print("OK, goodbye.")