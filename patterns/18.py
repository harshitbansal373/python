n=int(input("number of rows: "))
for i in range(n,0,-1):
  for j in range(n,0,-1):
    if j>=i:
      print(j,end='')
    else:
      print(i,end='')

  for j in range(2,n+1):
    if j>=i:
      print(j,end='')
    else:
      print(i,end='')
  print()

for i in range(2,n+1):
  for j in range(n,0,-1):
    if j>=i:
      print(j,end='')
    else:
      print(i,end='')

  for j in range(2,n+1):
    if j>=i:
      print(j,end='')
    else:
      print(i,end='')
  print()

'''
output-

555555555
544444445
543333345
543222345
543212345
543222345
543333345
544444445
555555555

'''
