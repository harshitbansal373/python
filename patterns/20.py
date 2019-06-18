n=int(input())
for i in range(1,n+1):
  if i!=n:
    print('*'*2,' '*(n-1),'*'*2,sep='')
  else:
    print('*'*(n+3),sep='')

for i in range(n,0,-1):
  if i!=n:
    print('*'*2,' '*(n-1),'*'*2,sep='')
  else:
    print('*'*(n+3),sep='')


'''
output-

**    **
**    **
**    **
**    **
********
********
**    **
**    **
**    **
**    **

'''
