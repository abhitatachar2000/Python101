"""
Write a program to input an integer from the user and determine the factorial of that number. 
The program should then output the factorial of the number.
"""
#I have provied two approaches to find the factorial of a number

def factorial(number): #This is the iterative approach
    factorial = 1;
    for i in range(1, number+1):
        factorial = factorial*i
    return factorial

def alternateApproachFactorial(number): #This is the recurssive approach
    if number ==0 or number ==1:
        return 1
    else:
        return number * factorial(number - 1)

number = int(input("Enter a number to find the factorial: "))
print(factorial(number))
print(alternateApproachFactorial(number))


