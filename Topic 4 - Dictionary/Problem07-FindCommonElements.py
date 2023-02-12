"""
Write a program to find the intersection of two dictionaries, 
and return a new dictionary with only the common key-value pairs.
"""

def findCommonElements(aDict, bDict):
    newDict = {}
    aKeys = aDict.keys()
    bKeys = bDict.keys()
    for i in aKeys:
        if i in bKeys:
            newDict[i] = aDict[i] + bDict[i]
        else:
            pass
    return newDict

aDict = {'a':1, 'b':2, 'c':4}
bDict = {'a':3, 'c':3, 'd':10}
print(findCommonElements(aDict, bDict))
