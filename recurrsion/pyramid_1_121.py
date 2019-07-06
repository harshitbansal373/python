def f(n,i):
  if n==0:
    return
  def g(t):
    if t==0:
      return
    g(t-1)
    if t>n:
      print(2*n-t,end='')
    else:
      print(t,end='')
  f(n-1,i+1)
  print(' '*i,sep='',end='')
  x=(2*n)-1
  g(x)
  print()

n=int(input("enter a number: "))
i=0
f(n,i)

'''
output-
enter a number: 8
       1
      121
     12321
    1234321
   123454321
  12345654321
 1234567654321
123456787654321

'''
