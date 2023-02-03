"""
Write a program that takes two strings as input from the user, and checks if one string is a substring of the other.
"""
def isSubString(mainString, subString):
    mainString = mainString.lower()
    subString = subString.lower() # performing a case insensitive search
    subStringCount = mainString.find(subString)
    if subStringCount != -1:
        return True
    else:
        return False

mainString = input("Enter the prinmary string: ")
subString = input("Enter the substring that has to be checked for: ")
if (isSubString(mainString, subString)):
    print("{0} is a substring of {1}".format(subString, mainString))
else:
    print("{0} is not a substring of {1}".format(subString, mainString))