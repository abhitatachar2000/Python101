"""
Write a program that takes a string as input from the user, and splits it into a list of words, 
removing any words that contain a given character.
"""

def removeSpecificWords(inputString, character):
    splitArray = inputString.split()
    for i in splitArray:
        if i.find(character) !=-1:
            splitArray.remove(i)
        else:
            pass
    returnString = " ".join(splitArray)
    print(returnString)

removeSpecificWords("Hello world, my name is Abhishek.", "o")   