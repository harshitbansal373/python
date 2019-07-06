def f(n):
  if n==0:
    return
  def g(t):
    if t==0:
      return
    print(t,end=' ')
    g(t-1)
  g(n)
  print()
  f(n-1)

n=int(input("enter a number: "))
f(n)

'''
output-
enter a number: 5
1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1 

'''
