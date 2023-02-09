"""
Write a program that takes a string as input from the user, and replaces all instances of a given word with a different word, ignoring case
"""
def replaceWords(inputString, searchWord, replaceWord):
    inputString, searchWord, replaceWord = removeAllPunctuations(inputString.lower()), searchWord.lower(), replaceWord.lower()
    stringArray = inputString.split()
    for i in stringArray:
        if i == searchWord:
            elementIndex = stringArray.index(i)
            stringArray[elementIndex] = replaceWord
    returnString = " ".join(stringArray)
    return returnString

mainString = input("Enter a string (Do not include punctuations): ")
searchWord = input("Enter the word to be searched: ")
replaceWord = input("Enter the replacing word: ")
print(replaceWords(mainString, searchWord, replaceWord))

