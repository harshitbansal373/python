n=int(input("enter the year: "))
if n%400==0 or n%100!=0 and n%4==0:
  print(n,"is leap year")
else:
  print(n,"is not leap year")
