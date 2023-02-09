"""
Write a program that takes two positive integers as input from the user and calculates 
their greatest common divisor (GCD). The program should print the calculated GCD.
"""
#We are using the Euclidian Algorithm to find the GCD of two numbers
def gcd(number1, number2):
    if (number2 == 0):
        return number1
    else:
        return gcd(number2, number1%number2)

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
print("GCD of "+str(number1)+" and "+str(number2)+" is "+str(gcd(number1, number2)))
    