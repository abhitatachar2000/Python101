"""
Write a program for storing the user details in a nested dictionary. 
The keys for the outer dictionary are the names of the user, 
the values for these keys are the inccer dictionary that holds the details of the users.
"""

userDirectory = {}

def addNewUser():
    global userDirectory
    name = input("Enter user name: ")
    userDetails = {}
    userDetails['age'] = input("Enter user age: ")
    userDetails['address'] = input("Enter user address: ")
    userDetails['phone'] = input("Enter user phone number: ")
    userDirectory[name] = userDetails

def deleteUser():
    global userDirectory
    name = input("Enter the user name: ")
    del userDirectory[name]

flag = True
while(flag):
    option = int(input("Enter 1 to enter the new user \nEnter 2 to delete user \nEnter 3 to exit \n: "))
    if option == 1:
        addNewUser()
        print(userDirectory)
    elif option == 2:
        deleteUser()
        print(userDirectory)
    elif option == 3:
        exit()
    