"""
Write a program that takes a dictionary of names and salaries as input from the user, and returns 
a dictionary with the names and salaries of the people who have a salary greater than a given amount.
"""

def findSal(aDict, sal):
    names = []
    for i in aDict.items():
        if i[1] > sal:
            names.append(i[0])
        else:
            pass
    return names

saLDict = {"alex":20000, "mike":25000, "jim":27000, "alpha":26500}
thresholdSal = 26000
print(findSal(saLDict, thresholdSal))