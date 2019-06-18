n=int(input())
for i in range(1,n+1):
  value=i
  extra=n-1
  for j in range(1,i+1):
    print(value,end='')
    value=value+extra
    extra=extra-1
  print()

'''
output-

1
27
3812
491316
510141719
61115182021

'''
