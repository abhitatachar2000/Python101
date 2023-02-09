"""
Write a program that takes a string as input from the user, and inserts a given character at a specified index.
"""

def insertAtIndex(inputString, character, index):
    #Divide the inputString into two parts 0 to index-1 and index to length of the string
    #Add the character in between the two parts 
    returnString = inputString[0:index] + character + inputString[index:]
    return returnString

print(insertAtIndex("abdef",'c',2))
