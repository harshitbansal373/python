a=int(input())
b=int(input())
A=[]
B=[]
for i in range(2,a+1):
  while True:
    if a%i==0:
      A.append(i)
      a=a//i
    else:
      break
for i in range(2,b+1):
  while True:
    if b%i==0:
      B.append(i)
      b=b//i
    else:
      break
hcf=1
for i in A:
  if i in B:
    hcf=hcf*i
print("HCF = ",hcf)
