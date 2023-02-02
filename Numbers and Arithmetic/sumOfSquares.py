"""
Write a program that finds the sum of squares of first n numbers
"""

import math
def findSumOfSquares(number):
    squareSum = 0
    for i in range(1, number+1):
        squareSum = squareSum + math.pow(i, 2)
    return int(squareSum)

number = int(input("Enter a number: "))
print("Sum of square of first {0} numbers is {1}".format(number, findSumOfSquares(number)))