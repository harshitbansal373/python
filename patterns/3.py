n=int(input("enter number of rows: "))
for i in range(1,n+1):
  print(' '*(n-i),'*'*i,sep='')

'''output
    *
   **
  ***
 ****
*****
'''
