r,c=map(int,input("enter number of rows and cols: ").split())
s=[]
print("enter matrix elements-")
for i in range(r):
   l=[]
   for j in range(c):
     a,b=map(int,input(f"enter a[{i}][{j}] b[{i}][{j}] :").split())
     l.append(a+b)
   s.append(l)
print()

for row in s:
  for n in row:
    print(n,end='\t')
  print()

'''
output-

enter number of rows and cols: 2 2
enter matrix elements-
enter a[0][0] b[0][0] :1 5
enter a[0][1] b[0][1] :2 6
enter a[1][0] b[1][0] :3 7
enter a[1][1] b[1][1] :4 8

6	8	
10	12	

'''
