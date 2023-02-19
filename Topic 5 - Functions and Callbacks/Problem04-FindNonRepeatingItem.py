#Write a Python function that takes a list of integers and 
#returns the index of the first non-repeating integer in the list. If all the integers are repeated, the function should return -1.

def findNonRepeatingItem(aLists):
	countDict = {}
	for i in aLists:
		if i in countDict.keys():
			countDict[i] = countDict[i] + 1
		else:
			countDict[i] = 1
	
	for (key, value) in countDict.items():
		if value == 1:
			return key
		else:
			pass
	return -1

aLists = [1, 1, 2, 3, 3, 3, 4, 4, 4]
print(findNonRepeatingItem(aLists)) #2 is the first non repeating integers

aLists = [1, 1, 2, 2, 3, 3, 4, 4, 4]
print(findNonRepeatingItem(aLists)) #All the numbers are repeated, so in this case -1 is returned
