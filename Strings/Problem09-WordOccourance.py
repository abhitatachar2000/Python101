"""
Write a program that takes a string as input from the user, and calculates the number of 
times a given word appears in it.
"""

def findNumberOfOccourance(inputString, word):
    stringCopy = inputString
    count = 0
    if(stringCopy.find(word) == -1):  #If the word is not found in the string
        print("{0} not found in '{1}'".format(word, stringCopy))
    else:
        wordLength = len(word)
        while (stringCopy.find(word)!=-1): #If the string is found
            count = count + 1 #Increment the count
            index = stringCopy.find(word)
            stringCopy = stringCopy[index+count:] 
            #The previous line will reassign the stringCopy to it's sliced version, such that the new
            #string will begin where the first occourance of the word ended.
        print("{0} is found in '{1}' {2} times".format(word, inputString, count))

findNumberOfOccourance("I want to have chocolates, chocolates are fun!", "chocolates")