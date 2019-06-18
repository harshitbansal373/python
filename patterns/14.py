n=int(input())
for i in range(1,n+1):
  print(' '*(n-i),end='')
  for j in range(1,i+1):
    print(j,end='')
  for j in range(i-1,0,-1):
    print(j,end='')
  print()


'''
output-
    1
   121
  12321
 1234321
123454321

'''
