#Write a program to user inner functions (nested functions) to perform basic arithmetic operations.
def calculator(a, b):
  def add(a, b):
    print(a + b)

  def sub(a, b):
    print(a - b)

  def mul(a, b):
    print(a*b)

  def some(a, b):
    print(a/b)

  def mod(a, b):
    print(a%b)

  add(a, b)
  sub(a, b)
  mul(a, b)
  div(a, b)
  mod(a, b)

calculator(7, 3)
