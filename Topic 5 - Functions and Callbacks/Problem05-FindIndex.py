#Create a Python function that takes a list of integers and returns a list of tuples, where each tuple contains the 
#index of the first occurrence and the index of the last occurrence of each unique integer in the list.

def findFirstAndLastIndex(aLists, number):
	if number in aLists:
		indexValueList = list(enumerate(aLists))
		reverseIndexValueList = indexValueList[::-1]
		for i in indexValueList:
			if i[1] == number:
				firstIndex = i[0]
				break;
		for j in reverseIndexValueList:
			if j[1] == number:
				lastIndex = j[0]
				break;
		return(firstIndex, lastIndex)
	else:
		return (None, None)

aLists = [1, 7, 4, 6, 3, 7, 9, 3, 8]
print(findFirstAndLastIndex(aLists, 7))
print(findFirstAndLastIndex(aLists, 15))
