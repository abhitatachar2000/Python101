"""
Write a program that takes a positive integer n as input from the user and generates the first n numbers in the Fibonacci series. 
The program should print each number in the series on a new line.
"""
def fibonacci(number):
    if number < 0:
        print("Incorrect input")
    if number == 1 or number == 0:
        return (number)
    else:
        return fibonacci(number-1) + fibonacci(number-2)

number = int(input("Enter a number: "))
#We want to print the fibonacci series for first n numbers, so we iterate for n numbers and then print for each number
for i in range (0, number+1):
    print(fibonacci(i))