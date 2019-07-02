'''
problem--
sample input-
-123ab45
ouput-
-12345
'''

n=input("enter number: ")
if n[0]=='-':
  print(n[0],end='')
for i in range(0,len(n)):
  if ord(n[i])>=48 and ord(n[i])<=57:
    print(n[i],end='')
print('\n')
