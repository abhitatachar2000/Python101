#Write a python function that takes a list and a callback function. The callback function 
#should be applied on each element of the list and the operated list should be printed on the screen.

def listOperation(aLists, operation):
  for i in aLists:
    operation(i)

def isOddOrEven(number):
  if number % 2 ==0:
    print("{0} is even number".format(number))
  else:
    print("{0} is odd number".format(number))

def isPrime(number):
  count = 0
  for i in range(1, number+1):
    if number%i == 0:
      count += 1
  if count == 2:
    print("{0} is a prime number".format(number))
  else:
    print("{0} is not a prime number".format(number))

aLists = list(range(1, 21))
listOperation(aLists, isOddOrEven)
