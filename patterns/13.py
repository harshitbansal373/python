n=int(input("enter number of rows: "))
for i in range(1,n+1):
  for j in range(n-i+1,n+1):
   print(j,end='')
  print()

'''output
5
45
345
2345
12345
'''
