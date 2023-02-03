"""
Write a program that takes a string as input from the user, and replaces all spaces with underscores.
"""

def replaceSpaceByUnderscore(inputString):
    returnString = '_'
    stringArray = inputString.split(" ") #splitting the array on sapces
    returnString = returnString.join(stringArray) #Joining the array with underscores
    return returnString

inputString = input("Enter a string having multiple words seperated by spaces: ")
result = replaceSpaceByUnderscore(inputString)
print(result)