"""
Write a program that takes a list of numbers as input from the users and returns 
another list that has no duplicate items.
"""

def removeDuplicateItems(aList):
    # Easy appoach is to do is to convert the list into a set and then again convert back to list
    # Let us go the iterative way here again
    noDuplicateList = []
    for i in aList:
        if i in noDuplicateList:
            pass
        else:
            noDuplicateList.append(i)

    return noDuplicateList

listLength = int(input("Enter the number of elements in the list: "))
inputList = [int(input("Enter element {0}: ".format(i+1))) for i in range(0, listLength)]
print("List without duplicate elements is: {0}".format(removeDuplicateItems(inputList)))