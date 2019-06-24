n=int(input("enter number: "))
c=0
while n:
  c=c*10+n%10
  n=n//10
print("reverse of number: ",c)

