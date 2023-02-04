"""
Write a program that takes a string as input from the user, and generates a new string by rearranging its characters in alphabetical order.
"""

def reorderString(inputString):
    stringArray = [i for i in inputString]
    stringArray.sort()
    returnString = ''
    for i in range(0,len(inputString)):
        returnString = returnString + stringArray[i]
    return returnString

print(reorderString("Hello World"))
