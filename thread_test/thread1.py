import threading

class myThread(threading.Thread):
    def __init__(self, target, *args):
        self._target = target
        self._args = args
        threading.Thread.__init__(self)
    def run(self):
        self._target(*self._args)

def f1(count):
    print 'Starting thread1\n'
    while count:
        print 'I am function1\n'
        count -= 1
    print 'Exiting thread2\n'
def f2(count):
    print 'Starting thread2\n'
    while count:
        print 'I am function2\n'
        count-= 1
    print 'Exiting thread2\n'

t1 = myThread (f1, 10)
t2 = myThread (f2, 12)
t1.start()
t2.start()
print "Exiting Main Thread"

