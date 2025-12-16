"""
Python Concurrency Guide
========================

Concurrency: The ability of a program to perform multiple tasks at the same time. 
In Python, concurrency can be achieved mainly in two ways:
1. Multithreading is the ability of a program to perform multiple tasks at the same time
    multithreading is better for I/O-bound tasks
2. Multiprocessing is the ability of a program to perform multiple tasks at the same time
    multiprocessing is better for CPU-bound tasks
General workflow:
- Create threads or processes
- Use attributes & methods
- Utilities & pools
- Handle race conditions & synchronization
- Interprocess communication (IPC)
"""
""" 
=========================== threading ============================
Python-এ থ্রেড হল একই প্রসেসের মধ্যে একাধিক ফাংশন বা কোড ব্লক একসাথে চালানোর একটি উপায়। 
মূলভাবে Python-এ থ্রেডিং দুইভাবে করা যায়: 
    threading মডিউল এবং concurrent.futures.ThreadPoolExecutor।
    
target → কোন ফাংশন চালাতে হবে।

args → ফাংশনের আর্গুমেন্ট tuple আকারে দিতে হবে।

start() → থ্রেড শুরু করে।

join() → মূল প্রোগ্রাম থ্রেড শেষ না হওয়া পর্যন্ত অপেক্ষা করে।

===================== race condition ======================
import threading
import time

balance = 0

def add_money(amount):
    global balance
    local_balance = balance
    local_balance += amount
    time.sleep(1)  # Simulate some processing
    balance = local_balance
    print(f"Balance updated to {balance} by {threading.current_thread().name}")

# দুইটি থ্রেড একই সময়ে balance পরিবর্তন করবে
thread1 = threading.Thread(target=add_money, args=(100,), name="T1")
thread2 = threading.Thread(target=add_money, args=(200,), name="T2")

thread1.start()
thread2.start()
thread1.join()
thread2.join()

print("Final Balance:", balance)

Race condition হল একটি সমস্যা, যখন একাধিক থ্রেড একই ডেটা বা রিসোর্স একসাথে অ্যাক্সেস করতে পারে, 
তখন ডেটা কনফ্লিক্ট বা ভুল ফলাফল এড়াতে Lock ব্যবহার করা হয়।

সমস্যা দেখা যায়:

মনে করুন balance শুরুতে 0।

T1 এবং T2 একসাথে balance পড়ে নিলো, এবং তাদের local_balance আলাদাভাবে আপডেট হলো।

ফলাফল হতে পারে 100 বা 200, কিন্তু 300 হওয়া উচিত।

এটা হলো race condition।
=========================== lock ============================
balance = 0
lock = threading.Lock()

def add_money_safe(amount):
    global balance
    with lock:  # এক সময়ে এক থ্রেডের এক্সেস নিশ্চিত
        local_balance = balance
        local_balance += amount
        time.sleep(1)
        balance = local_balance
        print(f"Balance safely updated to {balance} by {threading.current_thread().name}")

thread1 = threading.Thread(target=add_money_safe, args=(100,), name="T1")
thread2 = threading.Thread(target=add_money_safe, args=(200,), name="T2")

thread1.start()
thread2.start()
thread1.join()
thread2.join()

print("Final Balance (safe):", balance)

Lock একটি সিন্যাল যা একটি থ্রেড একসাথে একটি ফাংশন বা কোড ব্লক চালানোর সময় বাধা করে।
Python-এ Lock হলো একটি থ্রেড-সেফটি (thread-safety) মেকানিজম। সহজভাবে বললে, 
যখন একাধিক থ্রেড একই ডেটা বা রিসোর্স একসাথে অ্যাক্সেস করতে পারে, 
তখন ডেটা কনফ্লিক্ট বা ভুল ফলাফল এড়াতে Lock ব্যবহার করা হয়।

1. Lock কীভাবে কাজ করে

Lock একটি flag এর মতো যা বলে “এই রিসোর্সে কেউ কাজ করছে, অন্য কেউ অপেক্ষা করবে”।

যদি এক থ্রেড Lock পেয়ে কাজ শুরু করে, অন্য থ্রেড লক মুক্ত না হওয়া পর্যন্ত অপেক্ষা করবে।

with lock: → এক থ্রেড কাজ করছে, অন্য থ্রেড অপেক্ষা করবে।

Lock না থাকলে একসাথে দুই থ্রেড balance চেঞ্জ করার সময় ভুল মান আসতে পারে।

Lock থ্রেডগুলোর মধ্যে সেফ ডেটা এক্সেস নিশ্চিত করে।

একসাথে একাধিক থ্রেড এক ডেটা পরিবর্তন করতে পারবে না।

Python এ threading.Lock() ব্যবহার করা হয়।
2. Lock কে কেন ব্যবহার করতে হবে

Lock ব্যবহার করতে হবে যখন একাধিক থ্রেড একই ডেটা বা রিসোর্স একসাথে অ্যাক্সেস করতে পারে।

=========================== r lock ============================
import threading
import time

rlock = threading.RLock()

def recursive_task(n):
    if n > 0:
        with rlock:  # RLock ব্যবহার
            print(f"{threading.current_thread().name} acquired lock, n={n}")
            time.sleep(0.5)
            recursive_task(n-1)  # recursive call
    else:
        print(f"{threading.current_thread().name} finished recursion")

thread = threading.Thread(target=recursive_task, args=(3,), name="RThread")
thread.start()
thread.join()



Python-এ RLock মানে Reentrant Lock। এটা Lock এর মতোই, কিন্তু এর একটা বিশেষ ক্ষমতা আছে:

ReentrantLock একটি Lock যা একটি থ্রেড একসাথে একটি ফাংশন বা কোড ব্লক চালানোর সময় বাধা করে।
RLock কী?

সাধারণ Lock এক থ্রেডকে একসাথে একাধিক বার lock নেওয়া অনুমতি দেয় না।

কিন্তু RLock একই থ্রেড একাধিক বার lock acquire করতে পারে।

এই সুবিধা দরকার হয় যখন recursive function বা nested function call এক থ্রেডের মধ্যে একই lock ব্যবহার করে।

=========================== semaphore ============================

Python-এ Semaphore হলো একটি synchronization primitive যা থ্রেডগুলোকে একসাথে সীমিত সংখ্যক রিসোর্স ব্যবহার করার অনুমতি দেয়। সহজভাবে বললে, এটা বলে “এই রিসোর্সে একসাথে N জন ব্যবহারকারী থাকতে পারবে, বাকি থ্রেডগুলো অপেক্ষা করবে।”

Semaphore কী?

threading.Semaphore(value) – এখানে value হলো কতজন থ্রেড একসাথে resource ব্যবহার করতে পারবে।

যখন একটি থ্রেড semaphore acquire করে, value ১ কমে যায়।

যখন থ্রেড release করে, value ১ বৃদ্ধি পায়।

যদি value 0 হয়, অন্য থ্রেড acquire করার জন্য ব্লক হয়ে অপেক্ষা করবে।

 উদাহরণ
import threading
import time

# Semaphore value=2 → একসাথে maximum 2 থ্রেড কাজ করতে পারবে
sem = threading.Semaphore(2)

def task(name):
    print(f"{name} waiting to acquire semaphore...")
    with sem:
        print(f"{name} acquired semaphore!")
        time.sleep(2)
        print(f"{name} releasing semaphore...")

threads = []
for i in range(5):
    t = threading.Thread(target=task, args=(f"Thread-{i}",))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("All threads finished!")


ফলাফল :

Semaphore value 2, তাই একসাথে শুধু 2 থ্রেড কাজ করবে।

বাকি থ্রেডগুলো অপেক্ষা করবে যতক্ষণ না একটি থ্রেড release করে।

========================= Thread Lifecycle =========================
Thread Lifecycle in Python

একটি থ্রেড সাধারণত নিচের ধাপগুলো পার করে 

New → Runnable → Running → Blocked/Waiting → Terminated

New (Born / Created)

থ্রেড তৈরি করা হয়েছে, কিন্তু এখনো start() করা হয়নি।

import threading

def work():
    print("Thread working...")

t = threading.Thread(target=work)
print("Thread state: Created (New)")


এই অবস্থায় থ্রেড memory-তে আছে কিন্তু এখনো CPU পায়নি।

Runnable (Ready to Run)

থ্রেড start() করার পর CPU শিডিউলার থ্রেডটিকে রান করার জন্য প্রস্তুত রাখে।

t.start()
print("Thread state: Runnable")


এখন থ্রেড রান করার জন্য অপেক্ষায় আছে, কিন্তু এখনো চালু হয়নি (CPU scheduler-এর উপর নির্ভর করে কবে চালু হবে)।

Running

থ্রেড CPU পেয়ে ফাংশনের ভিতরের কাজ শুরু করে।

def work():
    print("Thread state: Running")


এখন থ্রেড তার টার্গেট ফাংশনের কাজ করছে।

Blocked / Waiting / Sleeping

থ্রেড অস্থায়ীভাবে থেমে গেছে— হয়ত I/O অপারেশন, sleep() বা অন্য থ্রেডের জন্য অপেক্ষা করছে।

import time

def work():
    print("Running...")
    time.sleep(2)  # থ্রেড এখন Waiting অবস্থায়
    print("Running again after sleep")


এ অবস্থায় থ্রেড CPU relinquish করে, কিন্তু জীবিত থাকে।

Terminated (Dead / Stopped)

থ্রেডের কাজ শেষ হয়ে গেলে সেটি বন্ধ হয়ে যায়।

t.join()
print("Thread state: Terminated")


একবার থ্রেড terminated হয়ে গেলে সেটিকে পুনরায় start করা যায় না।
(না হলে RuntimeError হবে)

চিত্র আকারে Thread Lifecycle
 ┌──────────────┐
 │   New        │
 └──────┬───────┘
        │ start()
        ▼
 ┌──────────────┐
 │  Runnable    │
 └──────┬───────┘
        │ (CPU scheduler)
        ▼
 ┌──────────────┐
 │   Running    │
 └──────┬───────┘
        │ sleep() / wait()
        ▼
 ┌──────────────┐
 │ Blocked/Wait │
 └──────┬───────┘
        │ resume / done
        ▼
 ┌──────────────┐
 │ Terminated   │
 └──────────────┘

সংক্ষেপে
Stage	Description
New	থ্রেড তৈরি হয়েছে কিন্তু শুরু হয়নি
Runnable	রান করার জন্য প্রস্তুত
Running	থ্রেড CPU পেয়ে চলছে
Waiting / Blocked	থ্রেড থেমে আছে (sleep, I/O, join ইত্যাদি কারণে)
Terminated	থ্রেড শেষ হয়েছে

============================== Thread Communication ===============================  

Python-এ Thread Communication মানে হচ্ছে — এক থ্রেড যেন অন্য থ্রেডের সাথে তথ্য আদান-প্রদান করতে পারে বা সিঙ্ক্রোনাইজ করতে পারে।

সাধারণভাবে থ্রেডরা আলাদা কাজ করে, কিন্তু অনেক সময় দরকার হয় তারা যেন “আপডেট শেয়ার” করতে পারে বা “অন্য থ্রেডের সিগন্যালের জন্য অপেক্ষা” করতে পারে।
এই কাজটাকেই বলে Thread Communication।

থ্রেড কমিউনিকেশনের প্রধান ৩টা পদ্ধতি
Method	ব্যবহার
Event	থ্রেডের মধ্যে সিগন্যাল পাঠানোর জন্য
Condition	এক থ্রেড অপেক্ষা করবে, অন্য থ্রেড notify করবে
Queue	থ্রেডদের মধ্যে নিরাপদ ডেটা ট্রান্সফার করার জন্য
1. Event — Signal Sending Between Threads

এক থ্রেড wait() করবে, আরেক থ্রেড set() করলে সে জেগে উঠবে।

import threading
import time

event = threading.Event()

def waiter():
    print("Waiter thread: Waiting for event...")
    event.wait()  # ইভেন্ট সেট না হওয়া পর্যন্ত থ্রেড থেমে থাকবে
    print("Waiter thread: Event received! Continuing...")

def setter():
    print("Setter thread: Doing some work...")
    time.sleep(3)
    event.set()  # ইভেন্ট সিগন্যাল পাঠালো
    print("Setter thread: Event set!")

t1 = threading.Thread(target=waiter)
t2 = threading.Thread(target=setter)

t1.start()
t2.start()
t1.join()
t2.join()


এখানে

event.wait() → থ্রেড অপেক্ষা করে

event.set() → অন্য থ্রেড সিগন্যাল দেয়

কাজ শুরু হয় set() করার পর

2. Condition — Wait এবং Notify মেকানিজম

এক থ্রেড অপেক্ষা করবে (wait()), আরেকটা থ্রেড notify() করে জাগাবে।

import threading
import time

condition = threading.Condition()
data_ready = False

def consumer():
    global data_ready
    with condition:
        print("Consumer waiting for data...")
        while not data_ready:
            condition.wait()  # ডেটা না আসা পর্যন্ত অপেক্ষা
        print("Consumer got the data!")

def producer():
    global data_ready
    time.sleep(3)
    with condition:
        print("Producer preparing data...")
        data_ready = True
        condition.notify()  # কনজিউমারকে সিগন্যাল পাঠানো

t1 = threading.Thread(target=consumer)
t2 = threading.Thread(target=producer)

t1.start()
t2.start()
t1.join()
t2.join()


এখানে

condition.wait() → অপেক্ষা করছে

condition.notify() → সিগন্যাল দিচ্ছে

খুব দরকার হয় “Producer-Consumer” প্যাটার্নে

Queue — Safe Data Sharing Between Threads

queue.Queue() থ্রেড-সেফ, তাই race condition হয় না।

import threading
import queue
import time

q = queue.Queue()

def producer():
    for i in range(5):
        print(f"Producer producing {i}")
        q.put(i)
        time.sleep(1)

def consumer():
    while True:
        item = q.get()
        print(f"Consumer got {item}")
        q.task_done()

t1 = threading.Thread(target=producer)
t2 = threading.Thread(target=consumer, daemon=True)

t1.start()
t2.start()
t1.join()
q.join()
print("All items processed!")


এখানে

q.put() → প্রডিউসার আইটেম দিচ্ছে

q.get() → কনজিউমার আইটেম নিচ্ছে

Queue নিজেই lock-managed, তাই নিরাপদ

সারসংক্ষেপ
Mechanism	ব্যবহার ক্ষেত্র
Event	এক থ্রেড অন্যকে সিগন্যাল দেয়
Condition	Wait–Notify সিস্টেম
Queue	ডেটা নিরাপদভাবে শেয়ার করা


একটা Real-life Example দেখাচ্ছি যেখানে Python-এ Thread Communication (Event, Condition, Queue) — সবগুলো ব্যবহার করে Producer–Consumer Model তৈরি করা হয়েছে।

এটা খুব জনপ্রিয় প্যাটার্ন, কারণ প্রায় সব multi-threaded অ্যাপেই (যেমন web server, background worker, order processing system ইত্যাদি) এই কনসেপ্টটা ব্যবহার হয়।

Producer–Consumer Example (Full Thread Communication Demo)
import threading
import queue
import time
import random

# Shared Queue (thread-safe)
task_queue = queue.Queue(maxsize=5)

# Event to signal when production stops
production_done = threading.Event()

# Condition to synchronize producer & consumer
condition = threading.Condition()


# Producer Thread
def producer():
    for i in range(1, 11):  # 10 টি আইটেম তৈরি করবে
        item = f"Task-{i}"
        with condition:
            while task_queue.full():
                print("Queue full, producer waiting...")
                condition.wait()  # কনজিউমারের জন্য অপেক্ষা
                
            task_queue.put(item)
            print(f"Producer produced: {item}")
            condition.notify_all()  # কনজিউমারকে জানানো
            
        time.sleep(random.uniform(0.5, 1.5))  # সময় নিচ্ছে
    
    # সব প্রডাকশন শেষ, ইভেন্ট সেট করা হলো
    production_done.set()
    print("Producer finished all tasks!")


# Consumer Thread
def consumer(name):
    while not (production_done.is_set() and task_queue.empty()):
        with condition:
            while task_queue.empty():
                if production_done.is_set():
                    return
                print(f"{name} waiting for items...")
                condition.wait()
                
            item = task_queue.get()
            print(f"{name} consumed: {item}")
            condition.notify_all()
        
        # প্রসেসিং সময় নিচ্ছে
        time.sleep(random.uniform(1, 2))
        task_queue.task_done()

    print(f"{name} finished consuming!")


# Main Section
producer_thread = threading.Thread(target=producer, name="Producer")
consumer_threads = [
    threading.Thread(target=consumer, args=(f"Consumer-{i}",))
    for i in range(1, 4)  # ৩ জন consumer
]

# সব থ্রেড চালু করা
producer_thread.start()
for t in consumer_threads:
    t.start()

# Join করা
producer_thread.join()
for t in consumer_threads:
    t.join()

print("\nAll production and consumption done successfully!")

কী হচ্ছে এখানে:
অংশ	কাজ
queue.Queue()	Producer এবং Consumer নিরাপদভাবে ডেটা শেয়ার করছে
Event (production_done)	Producer শেষ হলে সিগন্যাল পাঠাচ্ছে
Condition	Producer এবং Consumer একে অপরের জন্য wait/notify করছে
task_queue.put()	Producer আইটেম যোগ করছে
task_queue.get()	Consumer আইটেম নিচ্ছে
task_queue.task_done()	Consumer জানাচ্ছে কাজ শেষ

 """