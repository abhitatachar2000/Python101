"""
Write a program that takes the coordinates of two points in two-dimensional space as input from the user, 
and calculates the Euclidean distance between them. The program should print the calculated distance.
"""
#Euclidean Distance formula for a 2D space is Sqrt((x2-x1)^2 + (y2-y1)^2)
import math
def findEuclideanDistance(point1 , point2):
    return math.sqrt((point2[0]-point1[0])**2 + (point2[1]-point1[1])**2)

print("Input coordinates for point 1")
x1 = int(input("Enter the x-coordinate for point 1: "))
y1 = int(input("Enter the y-coordinate for point 1: "))
print("Input coordinates for point 2")
x2 = int(input("Enter the x-coordinate for point 2: "))
y2 = int(input("Enter the y-coordinate for point 2: "))
point1 = [x1, y1]
point2 = [x2, y2]
print(findEuclideanDistance(point1, point2))
