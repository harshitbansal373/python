import threading
import time
def f():
  print("hello")
  time.sleep(5)
t1=time.time()
for i in range(5):
  threading.Thread(target=f).start()
for t in threading.enumerate():
  if t.getName() in ['MainThread','SockThread']:
    continue
  t.join()
print(time.time()-t1)
