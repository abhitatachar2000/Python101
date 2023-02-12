"""
Write a program to find the difference of two dictionaries, and return a new dictionary with 
key-value pairs that exist in one but not the other.
"""

def findUniqueKeyValuePairs(aDict, bDict):
    uniqueDict = {}
    aKeys, bKeys = aDict.keys(), bDict.keys()
    for i in aKeys:
        if i in bKeys:
            pass
        else:
            uniqueDict[i] = aDict[i]
    for j in bKeys:
        if j in aKeys:
            pass
        else:
            uniqueDict[j] = bDict[j]

    return uniqueDict

aDict = {'a':2, 'b':4, 'c':6, 'd':5}
bDict = {'e':5, 'a':7, 'd':2, 'f':9}
print(findUniqueKeyValuePairs(aDict, bDict))
