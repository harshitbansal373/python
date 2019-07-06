def fact(n):
  if n==0:
    return 1
  return n*fact(n-1)

n=int(input("enter a number: "))
print(fact(n))

'''
output-
enter a number: 5
120

'''
