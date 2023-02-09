"""
Write a program that takes a list of strings and returns another list where the items 
are sorted in ascending order of their lengths.
"""

def orderStrings(aList):
    orderedList = []
    for item in aList:
        itemLength = len(item)
        if len(orderedList) == 0:
            orderedList.append(item)
        else:
            for index, value in enumerate(orderedList):
                if itemLength > len(value):
                    if index == len(orderedList) - 1:
                        orderedList.append(item)
                        break
                    else:
                        pass
                else:
                    orderedList = orderedList[:index] + [item] + orderedList[index:]
                    break
    return orderedList

listLength = int(input("Enter the length of the list: "))
aLists = [input("Enter string {}: ".format(i+1)) for i in range(0, listLength)]
print(orderStrings(aLists))
