"""
Write a program that takes a list of integers from the users and prints the second largest number in the list.
"""

def findSecondLargest(aList):
    aList = list(set(aList))
    aList.sort()
    return aList[-2]

listLength = int(input("Enter the number of elements in the list: "))
inputList = [int(input("Enter element {0}: ".format(i+1))) for i in range(0, listLength)]
print(findSecondLargest(inputList))