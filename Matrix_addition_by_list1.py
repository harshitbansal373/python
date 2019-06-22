r,c=map(int,input("enter number of rows and cols: ").split())
a=[]
print("enter first matrix elements-")
for i in range(r):
   l=[]
   for j in range(c):
     l.append(int(input(f"enter a[{i}][{j}] : ")))
   a.append(l)
print()

for row in a:
  for n in row:
    print(n,end='\t')
  print()
print()

b=[]
print("enter second matrix elements-")
for i in range(r):
   l=[]
   for j in range(c):
     l.append(int(input(f"enter b[{i}][{j}] : ")))
   b.append(l)
print()

for row in b:
  for n in row:
    print(n,end='\t')
  print()
print()

s=[]
print("sun of above two matrix-")
for i in range(r):
  l=[]
  for j in range(c):
    l.append(a[i][j]+b[i][j])
  s.append(l)

for row in s:
  for n in row:
    print(n,end='\t')
  print()

'''
output-

enter number of rows and cols: 2 2
enter first matrix elements-
enter a[0][0] : 1
enter a[0][1] : 2
enter a[1][0] : 3
enter a[1][1] : 4

1	2	
3	4	

enter second matrix elements-
enter b[0][0] : 5
enter b[0][1] : 6
enter b[1][0] : 7
enter b[1][1] : 8

5	6	
7	8	

sun of above two matrix-
6	8	
10	12	

'''
