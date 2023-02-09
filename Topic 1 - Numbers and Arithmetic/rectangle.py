"""
Write a program that takes the length and width of a rectangle as input from the user, 
and calculates its area and perimeter. The program should print the calculated area and perimeter.
"""
def findArea(length, breadth):
    return length * breadth

def findPerimeter(length, breadth):
    return 2 * (length + breadth)

length = int(input("Enter length: "))
breadth = int(input("Enter breadth: "))
print("Area = " +str(findArea(length, breadth))+" cms^2")
print("Perimeter = "+str(findPerimeter(length, breadth))+" cms")
