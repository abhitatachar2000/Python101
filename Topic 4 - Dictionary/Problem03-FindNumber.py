"""
Write a program that takes a dictionary of names and phone numbers as input from the user, 
and returns the phone number for a given name, or a message if the name is not found in the dictionary.
"""

def findNumber(phoneDict, phoneNumber):
    for i in phoneDict.items():
        if i[1] == phoneNumber:
            return i[0]
        else:
            pass

phoneDict = {"alex":9876543210, "mike":9632587401, "jim":7539516480, "alpha":7896541203}
print("The provieded phone number is of: {0}".format(findNumber(phoneDict, 7896541203)))