"""
Write a program to merge two dictionaries, combining values of keys with the same name and creating a new dictionary.
"""

def combineDict(dict1, dict2):
    combinedDict = dict1.copy()
    for i in dict2.keys():
        found = False
        for j in combinedDict.keys():
            if i == j:
                found = True
                combinedDict[j] = combinedDict[j] + dict2[i]
                break
        if found == False:
            combinedDict[i] = dict2[i]
    return combinedDict


dict1 = {"a": 1, "b":2, "c":3}
dict2 = {"d": 2, "e":2, "b":3}
print(combineDict(dict1, dict2))