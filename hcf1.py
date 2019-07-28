#Using Euclid's algorithm
print("Enter Two Numbers")
a=int(input())
b=int(input())
while True:
  if a==b:
    print("HCF = ",a)
    break
  if a>b:
    a=a-b
  else:
    b=b-a

