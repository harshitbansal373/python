r,c=map(int,input("enter number of rows and cols: ").split())
m=[]
print("enter matrix elements: ")
for i in range(r):
  l=[]
  for j in range(c):
    l.append(int(input(f"enter m[{i}][{j}]")))
  m.append(l)
print(m)
print()

for row in m:
  print(row)
print()

for row in m:
  for e in row:
    print(e,end='\t')
  print()

'''
output-

enter number of rows and cols: 3 4
enter matrix elements: 
enter m[0][0]1
enter m[0][1]2
enter m[0][2]3
enter m[0][3]4
enter m[1][0]5
enter m[1][1]6
enter m[1][2]7
enter m[1][3]8
enter m[2][0]9
enter m[2][1]0
enter m[2][2]1
enter m[2][3]2
[[1, 2, 3, 4], [5, 6, 7, 8], [9, 0, 1, 2]]

[1, 2, 3, 4]
[5, 6, 7, 8]
[9, 0, 1, 2]

1	2	3	4	
5	6	7	8	
9	0	1	2

'''
