n=int(input())
for i in range(1,n+1):
    if i!=n:
        print('*',' '*(n-2),'*'*n if i==1 else '*',sep='')
    else:
      print('*'*(2*n-1),sep='')

for i in range(2,n+1):
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
