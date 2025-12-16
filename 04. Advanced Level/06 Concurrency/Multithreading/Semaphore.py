# Semaphore is a synchronization primitive that controls access to a shared resource by multiple threads.
# Semaphore is a counter that is initialized to a positive value and can be decremented and incremented.
# Semaphore is used to limit the number of threads that can access a shared resource at the same time.
import threading
import time

semaphore = threading.Semaphore(2)
def task(semaphore):
    semaphore.acquire()
    print("Thread %s acquired semaphore" % threading.current_thread().name)
    time.sleep(5)
    semaphore.release()
    print("Thread %s released semaphore" % threading.current_thread().name)
t1 = threading.Thread(target=task, args=(semaphore,))
t2 = threading.Thread(target=task, args=(semaphore,))
t3 = threading.Thread(target=task, args=(semaphore,))
t4 = threading.Thread(target=task, args=(semaphore,))
t1.start()
t2.start()
t3.start()
t4.start()
t1.join()
t2.join()
t3.join()
t4.join()
