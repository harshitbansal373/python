n=input("enter alphabet: ")
if ord(n)>=65 and ord(n)<=90:
  n=chr(ord(n)+32)
else:
  n=chr(ord(n)-32)
print(n)

'''
output--
enter alphabet: g
G
enter alphabet: H
h
'''
