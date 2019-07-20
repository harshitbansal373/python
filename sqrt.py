#square root without function
n=int(input("enter a number: "))
for i in range(n):
  if i*i==n:
    print(i)
    break
  if i*i>n:
    j=i-1
    while j<=i:
      if j*j>n:
        print(j)
        break
      j=j+0.01
    break

'''
output--
enter a number: 99
9.94999999999998
'''
