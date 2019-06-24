n=int(input("enter number of elements: "))
l=[]
print("enter elements of list")
for i in range(n):
  l.append(int(input()))

x=int(input("enter element to remove: "))

while True:
  if x in l:
    l.remove(x)
  else:
    break
print(l)
