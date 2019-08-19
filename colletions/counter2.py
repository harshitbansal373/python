import collections
c=collections.Counter()
print('intial:',c)
c.update('abcdaab')
print('sequence:',c)
c.update({'a':1,'d':5,'f':10})
print("Dict:",c)
