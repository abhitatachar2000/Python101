"""
Build a calculator that can handle the four basic arithmetic operations 
(addition, subtraction, multiplication, and division) It should take two numbers and an 
operator as input, perform the calculation, and return the result.
"""
def calculator(firstNumber, secondNumber, operator):
    #Checks for the operator and then performs the operations accordingly
    if (operator=="+"):
        print("Sum of 2 numbers is: " + str(firstNumber + secondNumber))
    elif (operator=="-"):
        print("Difference of 2 numbers is: "+str(firstNumber - secondNumber))
    elif (operator=="*"):
        print("Product of 2 numbers is: "+str(firstNumber * secondNumber))
    elif (operator=="/"):
        print("Quotient is: "+str(firstNumber / secondNumber))

firstNumber = float(input("Enter the first number: "))  #User inputs first number
secondNumber = float(input("Enter the second number: ")) #User inputs second number
operator = input("Enter the operator: ") #User inputs operator
calculator(firstNumber, secondNumber, operator)
