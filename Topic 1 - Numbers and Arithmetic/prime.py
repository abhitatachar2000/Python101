"""
Write a program that takes an integer input from the user and determines if it is a prime number or not. 
The program should print 'Prime' if the number is prime, and 'Not Prime' if the number is not prime."

Condition: A number is prime if it is only divisible by 1 and itself. 
"""

def checkPrime(number):
    count = 0;
    for i in range(1, number+1):
        if (number % i == 0):
            count = count + 1
    if count == 2:
        print(str(number) + " is prime")
    else:
        print(str(number) + " is not prime")

number = int(input("Enter a number: "))
checkPrime(number)