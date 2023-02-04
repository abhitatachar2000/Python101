"""
Write a program that takes a string as input from the user, and removes all punctuation marks from it.
"""
def removeAllPunctuations(inputString):
    punctuations = ['.', ',', '?', ';', '!', ':', "'", '(', ')', '[', ']', '"', '...', '-', '-', '/', '@', '{', '}', '*']
    returnString = ""
    for i in inputString:
        if i in punctuations:
            pass
        else:
            returnString = returnString + i
    return returnString


print(removeAllPunctuations("Hi, Nice to meet you. How are you doing?"))

