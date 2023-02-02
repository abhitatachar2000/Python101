"""
Write a program that takes the coordinates of two points in two-dimensional space as input from the user, 
and calculates the slope of the line that passes through these two points. 
The program should print the calculated slope, rounded to two decimal places.
"""
# slope = rise/run = (y2-y1)/(x2-x1)
import math
def findSlope(point1, point2):
    m = (point2[1] - point1[1])/(point2[0]-point1[0])
    return m

print("Input coordinates for point 1")
x1 = int(input("Enter the x-coordinate for point 1: "))
y1 = int(input("Enter the y-coordinate for point 1: "))
print("Input coordinates for point 2")
x2 = int(input("Enter the x-coordinate for point 2: "))
y2 = int(input("Enter the y-coordinate for point 2: "))
point1 = [x1, y1]
point2 = [x2, y2]
print(findSlope(point1, point2))