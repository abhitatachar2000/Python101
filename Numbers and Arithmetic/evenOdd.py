"""
Write a program that takes an integer input from the user and determines if it is even or not. 
The program should print 'Even' if the number is even, and 'Odd' if the number is odd
"""
def determineEvenOdd(number):
    if number%2 == 0:
        print(str(number) + " is even")
    else:
        print(str(number) + " is odd")

number = int(input("Enter a number: "))
determineEvenOdd(number)