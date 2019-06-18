n1=int(input("enter first number: "))
n2=int(input("enter last number: "))
for n in range(n1,n2+1):
  for i in range(2,n//2+1):
    if n%i==0:
      break
  else:
    if n!=1:
      print(n,end='\t')
print()
