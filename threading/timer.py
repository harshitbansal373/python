import threading
import time
def hello():
  print("hello,timer")
if __name__=='__main__':
  t=threading.Timer(5,hello)
  t.start()
  t.join()
  print('main')

