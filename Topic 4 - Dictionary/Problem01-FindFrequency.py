"""
Write a program that takes a list of words as input from the user, and returns a dictionary with the 
frequency of each word in the list.
"""

def findFrequeny(aList):
    freqDict = {}
    for i in aList:
        i = i.lower()
        if i not in freqDict:
            freqDict[i] = 1
        else:
            freqDict[i] = freqDict[i] + 1
    return freqDict

listLength = int(input("Enter the length of list: "))
wordList = [input("Enter word {}: ".format(i+1)) for i in range(0, listLength)]
print(findFrequeny(wordList))