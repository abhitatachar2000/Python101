"""
Write a program that takes a string as input from the user, and capitalizes the first letter of each word. 
Do not use inbuilt method (string.title()) for the same.
"""

def makeTitleCase(inputString):
    returnString = ''
    i = 0
    while i < len(inputString):
        inputString = inputString.strip() #Ensuring that there is no sapce in the beinging of the sentence
        if i == 0:
            print(i)
            returnString = returnString + inputString[i].upper()
            i = i + 1
            continue
        if inputString[i] == " ":
            i+=1
            returnString = returnString + " " + inputString[i].upper()
        else:
            returnString = returnString + inputString[i]
        i = i+1
    return returnString

inputString = "hello world. nice to meet you."
print(makeTitleCase(inputString))