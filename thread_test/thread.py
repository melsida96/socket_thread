import thread

def f1():
    count = 0
    while count < 10:
        count += 1
        print 'f1 function'

def f2():
    count = 0
    while count < 10:
        count += 1
        print 'f2 function'

try:
    thread.start_new_thread(f1, ())
    thread.start_new_thread(f2, ())
except:
    print "error: unable to start thread"

while 1:
    pass


