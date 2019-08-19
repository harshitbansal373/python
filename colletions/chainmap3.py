import collections
a={'a':'A','c':'C'}
b={'b':'B','c':'D'}
m=collections.ChainMap(a,b)
print('before:',m)
m['c']='E'
print("after:",m)
print('a:',a)
print(type(a))
