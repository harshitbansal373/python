#using for recurrsion with less complexity
def power(n,m):
  if m==0:
    return 1
  if m==1:
    return n
  if m%2==0:
    return power(n*n,m//2)
  return n*power(n*n,(m-1)//2)
 
n=int(input("enter a number: "))
m=int(input("enter power: "))
print(power(n,m	))

'''
output--
enter a number: 2
enter power: 4
16
'''
