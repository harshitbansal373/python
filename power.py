#using for loop
n=int(input("enter a number: "))
m=int(input("enter power: "))
value=n
for i in range(1,m):
  value=value*n
print(value)

'''
output--
enter a number: 2
enter power: 4
16
'''
