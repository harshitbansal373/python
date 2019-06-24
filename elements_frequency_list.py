n=int(input("enter number of elements: "))
l=[]
print("enter elements of list")
for i in range(n):
  l.append(int(input()))

l1=[]
for i in l:
  if i not in l1:
    l1.append(i)

print("frequency of elements")
for i in l1:
  print(i,"--->",l.count(i))
