def determineEvenOdd(number):
    if number%2 == 0:
        print(str(number) + " is even")
    else:
        print(str(number) + " is odd")

number = int(input("Enter a number: "))
determineEvenOdd(number)