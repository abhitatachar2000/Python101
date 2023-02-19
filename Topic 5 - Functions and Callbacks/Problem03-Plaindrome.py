#Write a Python function to check whether a string is a pallendrome or not
def isPalindrome(aString):
	aString = aString.lower()
	reverseString = aString[::-1]
	if aString == reverseString:
		return True
	else:
		return False

aString = input("Enter a string: ")
if isPalindrome(aString):
	print("{0} is a plindrome".format(aString))
else:
	print("{0} is not a palindrome".format(aString))
