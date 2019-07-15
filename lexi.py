#lexi string codevita 2019

t=int(input())
l=[]
s=[]
for x in range(t):
  l.append(list(input()))
  s.append(list(input()))
for x in range(t):
  for i in l[x]:
    for h in range(len(s[x])):
      if i in s[x]:
        s[x].remove(i)
	print(i,end='')
  print()
