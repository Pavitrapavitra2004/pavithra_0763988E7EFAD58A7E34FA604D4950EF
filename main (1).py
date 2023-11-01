def isLeapYear (year):
  if (year%4==0 and year%100!=0) or Year%400==0:
     return True
  else:
     return False
Year=int (input ("Enter a year:"))
if isLeapYear (Year):
  print('{} is aLeapYeap.'.format(Year))
else:
   print ("{} is not a LeapYear.".format (Year))