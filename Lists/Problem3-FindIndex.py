"""
Write a program that takes a list of numbers as input from the users and 
returns the index of a given number in the list.
"""

def findIndex(aList, term):
    # The easiest way to find the index is use the index() function but let us use the linear search method
    found = False
    for index, value in enumerate(aList):
        if value == term:
            found = True
            return index
    if found == False:
        return -1
        

listLength = int(input("Enter the number of elements in the list: "))
inputList = [int(input("Enter element {0}: ".format(i+1))) for i in range(0, listLength)]
term = int(input("Enter the term to search: "))
print(findIndex(inputList, term))