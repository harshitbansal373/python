h=int(input("enter hour: "))
m=int(input("enter mintue: "))
if h!=12:
  hangle=(h*5*6)+(m/60)*30
else:
  hangle=(m/60)*30
mangle=m*6
angle=hangle-mangle
if angle<0:
  angle=-angle
print(angle)

'''
output--
enter hour: 3
enter mintue: 15
7.5
'''
