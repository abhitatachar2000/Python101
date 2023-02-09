"""
Write a program that takes a string as input from the user, and generates 
a new string by shifting each character in the string by a given number of positions.

Conditions for valid IPv4 - Its of the form xxx.xxx.xxx.xxx where each xxx is in the range of 0 - 255 
"""

def validIpV4Address(ipAddress):
    valid = True
    array = ipAddress.split('.')
    if len(array) == 4:
        for i in range(0, 4):
            if array[i].isdigit():
                array[i] = int(array[i])
            else:
                valid = False
                return valid
        for i in array:
            if i not in range(0, 256):
                valid = False
                return valid
    else:
        valid = False
    return valid

ipAddress = input("Enter a ipv4 address: ")
if(validIpV4Address(ipAddress)):
    print("{0} is a valid IPv4 address".format(ipAddress))
else:
    print("{0} is not a valid IPv4 address".format(ipAddress))