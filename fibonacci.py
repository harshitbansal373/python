n=int(input("enter number: "))
a=0
b=1
for i in range(n):
  print(a,end='\t')
  t=a+b
  a=b
  b=t
print()
