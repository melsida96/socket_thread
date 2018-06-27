import threading

class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print 'Starting ' + self.name 
        for i in range(0,10):
            print 'I am ' + self.name 
            i += 1
        print 'Exiting ' + self.name 

t1 = myThread (1, 'Thread1', 1)
t2 = myThread (2, 'Thread2', 2)
t1.start()
t2.start()
print "Exiting Main Thread"

