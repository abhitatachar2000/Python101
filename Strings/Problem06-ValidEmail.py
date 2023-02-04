"""
Write a program that takes a string as input from the user, and checks if it is a valid email address.
"""

def verifyValidEmail(emailAddress):
    #Check1 - The email address should not have spaces
    #Check2 - THe email should have a @, a set of characters before the @ and a set of characters after @
    #Check3 - The email ends with .com (assumption)
    valid = False
    if(emailAddress.count(" ")==0):
        emailSplit = emailAddress.split("@")
        if(len(emailSplit)==2):
            if emailSplit[1].endswith(".com"):
                valid = True
    return valid

emailAddress = input("Enter your email address: ")
if(verifyValidEmail(emailAddress)):
    print("Email address is valid")
else:
    print("Email address is not valid")



