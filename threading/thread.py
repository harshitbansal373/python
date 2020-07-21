import time
import threading
def f():
  print("hello",10,"class")
  time.sleep(5)
t1=time.time()
l=[]
for i in range(5):
  l.append(threading.Thread(target=f))
  l[-1].start()
for t in l:
  t.join()  
print(t)
t2=time.time()
print(t2-t1)
