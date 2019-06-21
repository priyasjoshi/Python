import threading
import datetime

class myThread(threading.Thread):
    def __init__(self,threadID,name,counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        threadLock.acquire()
        print('Starting' + self.name)
        print_date(self.name, self.counter)
        print('Exiting ' + self.name)
        threadLock.release()
def print_date(threadName,counter):
    today = datetime.date.today()
    print(threadName,counter,today)

threadLock = threading.Lock()
threads = []
thread1 = myThread(1,'Thread 1',1)
thread2 = myThread(2,'Thread 2',2)
threads.append(thread1)
threads.append(thread2)
#Start a new thread

thread1.start()
thread2.start()

for t in threads:
    t.join()
print('Exiting the program !!')