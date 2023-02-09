"""
Write a program that takes a string as input from the user, and returns a new string with 
all occurrences of a given character replaced by its opposite case.
"""

def swapCase(inputString):
    returnString = ''
    for i in inputString:
        if i.isalpha():
            if i.isupper():
                returnString = returnString + i.lower()
            elif i.islower():
                returnString = returnString + i.upper()
        else:
            returnString = returnString + i
    return returnString

print(swapCase("hEllo wORlD"))