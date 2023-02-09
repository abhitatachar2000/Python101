"""
Write a program that takes a string as input from the user, 
and removes all duplicate characters from it.
"""

def removeDuplicates(inputString):
    returnString = ''
    for i in inputString:
        if returnString.find(i) == -1: #If the character is not present in the string
            returnString = returnString + i #We add only the first occourance to the return string
        else:
            pass
    return returnString

print(removeDuplicates("abcdaaefbgh"))