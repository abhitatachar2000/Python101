"""
Write a program that takes a list of strings as input from the users and returns the 
longest string in the list.
"""

def findLongestString(aLists):
    longestString = aLists[0]
    maximumLength = len(aLists[0])
    for i in aLists:
        if len(i) > maximumLength:
            maximumLength = len(i)
            longestString = i
    return longestString

listLength = int(input("Enter the length of the list: "))
aLists = [input("Enter string {}: ".format(i+1)) for i in range(0, listLength)]
print("Longest string in the passed list is ", findLongestString(aLists))