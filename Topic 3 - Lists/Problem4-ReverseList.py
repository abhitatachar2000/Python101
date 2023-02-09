"""
Write a program that takes a list of numbers as input from the users and returns 
the reverse of the list.
"""

def reverseList(aList):
    #There are two easy approaches 
    # 1. Slice the list to reverse it aList[::-1]
    # 2. aList.reverse()
    # But for this example let us do the itterative way
    reverseList = []
    for i in range(len(aList)-1, -1, -1):
        reverseList.append(aList[i])
    print("Reversed list is {0}".format(reverseList))

listLength = int(input("Enter the number of elements in the list: "))
inputList = [int(input("Enter element {0}: ".format(i+1))) for i in range(0, listLength)]
reverseList(inputList)

