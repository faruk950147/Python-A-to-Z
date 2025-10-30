"""
Python Concurrency Guide
========================

Concurrency: The ability of a program to perform multiple tasks at the same time. 
In Python, concurrency can be achieved mainly in two ways:
1. Multithreading
2. Multiprocessing

General workflow:
- Create threads or processes
- Use attributes & methods
- Utilities & pools
- Handle race conditions & synchronization
- Interprocess communication (IPC)
"""

# =========================
# 1. Multithreading Example
# =========================
import threading
from multiprocessing import Process
import os
from concurrent.futures import ProcessPoolExecutor

def thread_worker():
    print(f"Thread {threading.current_thread().name} is running")

# Create a thread
t1 = threading.Thread(target=thread_worker, name="Thread-1")
t1.start()
t1.join()  # Wait until the thread finishes

# =========================
# 2. Multiprocessing Example
# =========================

def process_worker():
    print(f"Process PID {os.getpid()} is running")

p1 = Process(target=process_worker, name="Process-1")
p1.start()
p1.join()  # Wait until the process finishes

# =========================
# 3. Thread Race Condition Example
# =========================
counter = 0

def increment_counter():
    global counter
    for _ in range(1000):
        counter += 1  # Race condition may occur

threads = [threading.Thread(target=increment_counter) for _ in range(10)]
[t.start() for t in threads]
[t.join() for t in threads]
print("Race condition result:", counter)

# =========================
# 4. Thread Synchronization with Lock
# =========================
lock = threading.Lock()
counter = 0

def safe_increment():
    global counter
    for _ in range(1000):
        with lock:
            counter += 1  # Lock ensures safe access

threads = [threading.Thread(target=safe_increment) for _ in range(10)]
[t.start() for t in threads]
[t.join() for t in threads]
print("Synchronized result:", counter)

# =========================
# 5. Process Pool Example
# =========================

def square(n):
    return n * n

with ProcessPoolExecutor(max_workers=4) as executor:
    results = list(executor.map(square, range(10)))
print("Process Pool results:", results)

# =========================
# 6. Interprocess Communication (Queue)
# =========================
from multiprocessing import Queue

def worker_put(q):
    q.put(f"Hello from process {os.getpid()}")

queue = Queue()
p = Process(target=worker_put, args=(queue,))
p.start()
print(queue.get())  # Receive message
p.join()
