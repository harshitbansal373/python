import threading
import time
import numpy as np
def flag():
  time.sleep(3)
  event.set()
  print("starting countdown")
  time.sleep(7)
  event.clear()

def start_operation():
  event.wait()
  while event.is_set():
    print("starting random integer task")
    x=np.random.randint(1,30)
    time.sleep(1)
    if x==29:
      print("True")
  print("event has been cleared, random stops")
event=threading.Event()
t1=threading.Thread(target=flag)
t2=threading.Thread(target=start_operation)
t1.start()
t2.start()
t1.join()
t2.join()
print("All Done")
