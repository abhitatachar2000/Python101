"""
Write a program that takes a string as input from the user, and converts it to a list of integers representing the ASCII values of each character.
"""
#ord() converts char to ascii

def findAscii(inputString):
    returnString = ''
    for i in inputString:
        returnString = returnString + str(ord(i))
    return returnString
    
result = findAscii(input("Enter a string: "))
print(result)
