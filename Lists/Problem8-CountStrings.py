"""
Write a program that takes a list of strings as input from the user, and returns the count of all strings that start with a given letter.
"""

def countStrings(aList, char):
    count = 0
    for i in aList:
        if i.startswith(char):
            count = count + 1
        else:
            pass
    return count

listLength = int(input("Enter the number of elements in the list: "))
inputList = [input("Enter element {0}: ".format(i+1)) for i in range(0, listLength)]
char = input("Enter the character: ")
print("Numbers of elements starts with {0} is {1}".format(char, countStrings(inputList, char)))
