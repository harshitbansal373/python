n=int(input())
for i in range(1,n+1):
    if i!=n:
      if i>1:
        print('*',' '*(n-2),'*',sep='')
      else:
        print('*',' '*(n-2),'*'*n,sep='')
    else:
      print('*'*(2*n-1),sep='')

for i in range(n,0,-1):
    if i==n:
      print('*'*n,' '*(n-2),'*',sep='')
    else:
      print(' '*(n-1),'*',' '*(n-2),'*',sep='')


'''
output-

*   *****
*   *
*   *
*   *
*********
    *   *
    *   *
    *   *
*****   *

'''
