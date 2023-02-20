# Write a program that converts temperature from celcius to farenheit and vice versa based on a callback function.
def convertTemperature(temp, convertFunction):
  convertFunction(temp)

def celciusToFarenheit(temp):
  fahrenheit = temp * (9/5) + 32
  print("{0}C is {1}F".format(temp, fahrenheit))

def farenheitToCelcius(temp):
  celsius = (5/9)*(temp-32)
  print("{0}F is {1}C".format(temp, celsius))

convertTemperature(6, celciusToFarenheit)
convertTemperature(112, farenheitToCelcius)
