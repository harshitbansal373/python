import functools
import queue
import threading

class job:
  def __init__(self,priority,description):
    self.priority=priority
    self.description=description
    print('New Job:',description)
    return
  def __eq__(self,other):
    try:
      return self.priority==other.priority
    except AttributeError:
      return NotImplemented
  def __lt__(self,other):
    try:
      return self.priority<other.priority
    except AttributeError:
      return NotImplemented

q=queue.PriorityQueue()
q.put(job(3,'mid-level job'))
q.put(job(10,'low-level job'))
q.put(job(1,'important-level job'))

def process_job(q):
  while True:
    next_job=q.get()
    print('pocessing job:',next_job.description)
    q.task_done()

workers=[threading.Thread(target=process_job,args=(q,)), threading.Thread(target=process_job,args=(q,))]
for w in workers:
  w.setDaemon(True)
  w.start()
q.join()
