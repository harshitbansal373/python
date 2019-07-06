def fib(n):
  if n==0:
    return
  if n==1:
    return 0
  if n==2:
    return 1
  return fib(n-1)+fib(n-2)

n=int(input("enter a number: "))
print(fib(n))

'''
output-
enter a number: 5
3

'''
