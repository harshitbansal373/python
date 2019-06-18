n=int(input("enter number of rows: "))
for i in range(n,0,-1):
  for j in range(n-i+1,n+1):
   print(j,end='')
  print()

'''output
12345
2345
345
45
5
''' 
