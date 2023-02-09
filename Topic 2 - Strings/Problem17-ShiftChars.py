"""
Write a program that takes a string as input from the user, and generates a new string by 
shifting each character in the string by a given number of positions.
"""

def shiftCharacters(inputString, positions):
    shiftedString = inputString[positions:]
    for i in range(0, positions):
        shiftedString = shiftedString + inputString[i]
    return shiftedString

inputString = input("Enter the string: ")
positions = int(input("Enter the positions by which the characters have to be shifted: "))
print(shiftCharacters(inputString, positions))