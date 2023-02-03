"""
Write a program that takes a string as input from the user, and reverses the order of its characters.
"""

def stringReverse(inputString):
    result = ''
    for i in range(len(inputString)-1, -1, -1):
        result = result + inputString[i]
    return result

originalString = input("Enter a string: ")
print(stringReverse(originalString))

