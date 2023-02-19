#Write a Python function that takes a string and returns a new string with all the vowels removed. The function should use recursion to achieve this
def removeVovels(aString):
	aString = aString.lower()
	vovels = ['a', 'e', 'i', 'o', 'u']
	if len(aString) == 0:
		return ""
	else:
		if aString[0] in vovels:
			char = ""
		else:
			char = aString[0]
	return char + removeVovels(aString[1:])
 
print(removeVovels("Hello World"))
