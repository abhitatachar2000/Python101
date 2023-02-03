"""
Write a program that takes a string as input from the user, and checks if it is a palindrome. 
Reverse the string manually here and do not use inbuild methods for the same.
"""
#I have reused the part of code from ReverseString.py
def stringReverse(inputString):
    result = ''
    for i in range(len(inputString)-1, -1, -1):
        result = result + inputString[i]
    return result

def isPalindrome(inputString):
    inputString = inputString.lower() #Let's ignore the case of the string and convert it lower case
    reverseString = stringReverse(inputString)
    if inputString == reverseString:
        return True
    else:
        return False

inputString = input("Enter a string: ")
if(isPalindrome(inputString)):
    print("{0} is a palindrome".format(inputString)) #printing using the .format() method
else:
    print("%s is not a palindrome" %(inputString)) #printing using %s placeholder for strings