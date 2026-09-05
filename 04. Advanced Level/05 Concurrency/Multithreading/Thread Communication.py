# Thread Communication is a process where threads communicate with each other to coordinate their actions.

# 1. event
# 2. condition
# 3. semaphore
# 4. queue

# Event
# Event is a simple object that can be set and cleared.
# It is used to signal between threads.
import threading
import time
event = threading.Event()
""" 
def start():
    print("Thread is waiting for the event to be set.")
    time.sleep(5)
    event.set()
    print("Thread is processing the event.")
    
def stop():
    event.wait()
    if event.is_set():
        print("Thread is stopped.")
    
if __name__ == "__main__":
    t1 = threading.Thread(target=start)
    t2 = threading.Thread(target=stop)
    t1.start()
    t2.start()
    time.sleep(5)
    t1.join()
    t2.join()
    
def task(event):
    print("Thread is waiting for the event to be set.")
    event.wait()
    print("Thread is processing the event.")

if __name__ == "__main__":
    event = threading.Event()
    thread = threading.Thread(target=task, args=(event,))
    thread.start()
    time.sleep(5)
    event.set()
    thread.join()
 """
 
 
# Condition
# Condition is a more complex object that can be used to synchronize threads.
# It is used to coordinate the actions of threads.

condition = threading.Condition()

# Semaphore
# Semaphore is a more complex object that can be used to synchronize threads.
# It is used to limit the number of threads that can access a resource.

semaphore = threading.Semaphore(2)

# Queue
# Queue is a more complex object that can be used to transfer data between threads.

queue = threading.Queue()
