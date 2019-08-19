import collections
def default_factory():
  return 'default value'
d=collections.defaultdict(default_factory,a=3,b=7)
print('d:',d)
print('a:',d['a'])
print('b:',d['b'])
print('c:',d['c'])
print('d:',d['d'])
