n=int(input("enter number: "))
rev=0
d1=0
d2=0
d={0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
while n:
  rev=rev*10+n%10
  d1=d1+1
  n=n//10

while rev:
  print(d[rev%10],end=' ')
  d2=d2+1
  rev=rev//10

for i in range(d1-d2):
  print('zero',end=' ')
print()
