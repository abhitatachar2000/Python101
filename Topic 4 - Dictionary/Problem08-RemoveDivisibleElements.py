"""
Write a program to remove all key-value pairs in a dictionary that have values that are divisible by 3.
"""

def removeDivisibleElements(aDict):
    bDict = aDict.copy()
    for i in aDict.keys():
        if bDict[i] % 3 == 0:
            del bDict[i]
        else:
            pass
    return bDict

aDict = {'a':3, 'b':4, 'c':6, 'd':8, 'e':9}
print(removeDivisibleElements(aDict))