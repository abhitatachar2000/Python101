"""
Write a program that takes the radius of a circle as input from the user, and calculates its area and 
circumference. The program should print the calculated area and circumference, 
rounded to two decimal places.
"""

import math
def findArea(radius):
    pi = math.pi
    area = pi*math.pow(radius,2)
    return area

def findCircumference(radius):
    pi = math.pi
    circumference = 2*pi*radius
    return circumference

radius = float(input("Enter the radius in cms: "))
print("Area of the circle = "+str(findArea(radius))+ "cm^2")
print("Circumference of the circle = "+str(findCircumference(radius))+"cms")