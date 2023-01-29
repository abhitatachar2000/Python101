def checkLeap(year):
  leapYear = False
  if year%4 == 0: 
    leapYear = True 
    if year%100 == 0: 
      leapYear = False
      if year%400 == 0:
        leapYear = True
  return leapYear

year = int(input("Enter year: "))
result = checkLeap(year)
if(result):
  print("The year {0} is a leap year".format(year))
else:
  print("The year {0} is not a leap year".format(year))