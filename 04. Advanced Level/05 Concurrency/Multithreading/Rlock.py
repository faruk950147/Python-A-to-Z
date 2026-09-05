# Reentrant Lock is a type of lock that allows a thread to acquire the same lock multiple times without causing a deadlock.
# Reentrant Lock current thread can acquire the same lock multiple times.
import threading
import time

lock = threading.RLock()
def task(lock):
    lock.acquire()
    print("First lock acquired")
    lock.acquire()  
    print("Second lock acquired")
    time.sleep(5)
    lock.release()
    lock.release()
    print("Lock released")
t1 = threading.Thread(target=task, args=(lock,))
t2 = threading.Thread(target=task, args=(lock,))
t1.start()
t2.start()
t1.join()
t2.join()