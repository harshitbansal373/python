n=int(input("enter number of rows: "))
for i in range(1,n+1):
  print(' '*(i-1),i,' '*(n-2*i+4),i if i<n else '',sep='')
for i in range(n-1,0,-1):
  print(' '*(i-1),i,' '*(n-2*i+4),i,sep='')

'''output
1	1
 2     2
  3   3
   4 4
    5
   4 4
  3   3
 2     2
1	1

''' 
