"""
Write a program that takes three numbers as input from the user, and calculates the maximum 
and minimum among them. The program should print the maximum and minimum numbers.
"""

#Easy approcach would be to push the elemets to a list and use max() and min() functions
#But in this example we shall find it out manually

def findMaxMin(number1, number2, number3):
    if number1 > number2:
        if number2 > number3:
            print(str(number1) + " is the maximum number")
            print(str(number3) + "is the minimum number")
        elif number3 > number1:
            print(str(number3) + " is the maximum number")
            print(str(number2) + " is the minimum number")
        else:
            print(str(number1) + " is the maximum number")
            print(str(number2) + " is the minimum number")

    elif(number2>number3):
        print(str(number2) + " is the maximum number")
        if number3 > number1:
            print(str(number1) + "is the minimum number")
        else:
            print(str(number3) + "is the minimum number")
    else:
        print(str(number3) + " is the maximum number")
        print(str(number1) + "is the minimum number")


findMaxMin(32, 43, 15)