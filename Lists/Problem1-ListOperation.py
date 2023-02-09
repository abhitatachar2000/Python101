"""
Write a program that takes a list of numbers as a input from the users and performs the following operations:
- Find the sum of all the items in the list
- Find the average of all the items in the list
- Find the minimum item
- Find the maximum item
- Count the number of even numbers
- Count the number of odd numbers
"""

def findSum(aList):
    sum = 0
    for i in aList:
        sum = sum + i
    return sum

def findAverage(aList):
    sum = findSum(aList)
    average = sum/len(aList)
    return average

def findMinimumItem(aList):
    minimumItem = aList[0]
    for i in aList:
        if i < minimumItem:
            minimumItem = i
        else:
            pass
    return minimumItem

def findMaximumItem(aList):
    maximumItem = aList[0]
    for i in aList:
        if i > maximumItem:
            maximumItem = i
        else:
            pass
    return maximumItem

def countEvenNumbers(aList):
    count = 0
    for i in aList:
        if i % 2 == 0:
            count = count + 1
    return count

def countOddNumbers(aLists):
    count = 0
    for i in aLists:
        if i % 2 != 0:
            count = count + 1
    return count

listLength = int(input("Enter the number of elements in the list: "))
inputList = [int(input("Enter element {0}: ".format(i+1))) for i in range(0, listLength)]
print("Sum of elements is: {0}".format(findSum(inputList)))
print("Average of elements is: {0}".format(findAverage(inputList)))
print("Minimum of elements is: {0}".format(findMinimumItem(inputList)))
print("Maximum of elements is: {0}".format(findMaximumItem(inputList)))
print("Count of event elements is: {0}".format(countEvenNumbers(inputList)))
print("Count of odd elements is: {0}".format(countOddNumbers(inputList)))