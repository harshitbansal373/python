import threading
import time
import logging
logging.basicConfig(level=logging.DEBUG,format="%(threadName)-10s %(message)10s")
def f1():
  logging.debug('starting')
  time.sleep(1)
  logging.debug('exiting')

def f2():
  logging.debug('starting')
  time.sleep(2)
  logging.debug('exiting')

def f3():
  logging.debug('starting')
  time.sleep(3)
  logging.debug('exiting')
logging.debug('starting')
t1=threading.Thread(target=f1)
t2=threading.Thread(name='f2',target=f2)
t3=threading.Thread(name='f3',target=f3)
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
