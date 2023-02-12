"""
Write a program to find the minimum and maximum values in a dictionary, 
and return a tuple with the keys associated with those values.
"""

def findMinMax(aDict):
    aKeys = list(aDict.keys())
    minKey, maxKey = aKeys[0], aKeys[0]
    min, max = aDict[minKey], aDict[maxKey]
    for i in aKeys:
        if aDict[i] < min:
            min = aDict[i]
            minKey = i
        else:
            pass

        if aDict[i] > max:
            max = aDict[i]
            maxKey = i
        else:
            pass
    return (minKey, maxKey)

aDict = {'a':1, 'b':3, 'c':6, 'd':2, 'e': 8}
print(findMinMax(aDict))