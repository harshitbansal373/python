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
lcm=1
for i in A:
 lcm=lcm*i
 if i in B:
   B.remove(i)
for i in B:
  lcm=lcm*i
print("LCM = ",lcm)
