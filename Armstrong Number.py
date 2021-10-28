num = int(input())
temp = num
count = 0
while(num>0):
  res = num % 10
  count = count + res**3
  num = num//10
if(count == temp):
  print("Armstrong Number")
else:
  print("Not a Armstrong Number")
