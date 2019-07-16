class Node:
  def __init__(self):
    self.data=None
    self.next=None

class linkedlist:
  def __init__(self):
    self.start=None
  
  def createNode(self):
    while True:
      newnode=Node()
      newnode.data=int(input("enter data: "))
      if self.start==None:
        self.start=newnode
        current=newnode
      else:
        current.next=newnode
        current=newnode
      n=input("enter choice: ")
      if n in ['n','N']:
        break

  def Display(self):
    ptr=self.start
    while ptr!=None:
      print(ptr.data,end='\t')
      ptr=ptr.next

l=linkedlist()
l.createNode()
l.Display()
print()

'''
output--
enter data: 2
enter choice: y
enter data: 5
enter choice: y
enter data: 9
enter choice: n
2	5	9
'''
