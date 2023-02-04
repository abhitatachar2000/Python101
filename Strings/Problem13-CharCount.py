"""
Write a program that takes a string as input from the user, and generates a dictionary where each key is a letter in the string, 
and each value is the number of times that letter appears in the string, ignoring case.
"""

def charCount(inputString):
    inputString = inputString.lower()
    charDict = {}
    for i in inputString:
        if i.isalpha(): #Check if the character is an aplhabetc letter
            if i not in charDict:
                charDict[i] = 1
            else:
                charDict[i] = charDict[i] + 1
    print(charDict)

inputString = input("Enter a string: ")
print(charCount(inputString))