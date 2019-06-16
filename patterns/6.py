n=int(input("enter number of rows: "))
for i in range(1,n+1):
  print('*'*i,sep='')
for i in range(n-1,0,-1):
  print('*'*i,sep='')

'''output
*
**
***
****
*****
****
***
**
*
'''
