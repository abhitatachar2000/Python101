"""
Write a program that takes a string as input from the user, and removes all vowels from it.
"""

def removeVowels(inputString):
    vowels = ['a', 'e', 'i', 'o', 'u']
    inputString = inputString.lower() #Let's consider case insensitive search
    returnString = ''
    for i in inputString:
        if i in vowels:
            pass
        else:
            returnString = returnString + i
    return returnString

inputString = input("Enter a string: ")
result = removeVowels(inputString)
print(result)
