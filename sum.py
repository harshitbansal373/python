n=int(input("enter number: "))
sum=0
while n:
  sum=sum+n%10
  n=n//10
print("sum of digits: ",sum)
