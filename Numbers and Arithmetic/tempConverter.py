"""
Write a program that takes a temperature value and a unit of measurement (Celsius or Fahrenheit) as input from the user, 
and converts the temperature to the other unit of measurement. The program should print the converted temperature, 
rounded to two decimal places.
"""

def convertTemp(choice, temperature):
    if choice == 1:
        print("Converting temperature from Celsius to Fahrenheit")
        #Formula is F = C * (9/5) + 32
        fahrenheit = temperature * (9/5) + 32
        fahrenheit = round(fahrenheit, 2)
        print("{0}C is {1}F".format(temperature, fahrenheit))

    elif choice == 2:
        print("Converting temperature from Fahrenheit to Celsius")
        #Formula is 5(F - 32)/9
        celsius = (5/9)*(temperature-32)
        celsius = round(celsius, 2)
        print("{0}F is {1}C".format(temperature, celsius))

    else:
        print("Invalid choice")

choice = int(input("Enter 1 to convert Celsius to Fahrenheit or Press 2 for converting Fahrenheit to Celsius: "))
temp = int(input("Enter temperature: "))
convertTemp(choice, temp)

