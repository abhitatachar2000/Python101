"""
Write a program that takes a string as input from the user, and returns the first non-repeated character in the string.
"""
# I have reused the char count function from problem13
def charCount(inputString):
    inputString = inputString.lower()
    charDict = {}
    for i in inputString:
        if i.isalpha(): #Check if the character is an aplhabetc letter
            if i not in charDict:
                charDict[i] = 1
            else:
                charDict[i] = charDict[i] + 1
    return charDict

def findFirtstNonRepeatingChar(inputString):
    inputString = inputString.lower()
    charCountDict = charCount(inputString)
    for i in charCountDict.keys():
        if charCountDict[i] == 1:
            return i

inputString = input("Enter a string: ")
print(findFirtstNonRepeatingChar(inputString))