# ============================= Stack =============================
# Stack: Last In First Out (LIFO) structure
# Used for function calls and local variables (in Python, list can act as a stack)
# directly access is allowed

import heapq
import gc
stack = []
stack.append(10)  # push
stack.append(20)
stack.append(30)
print("Stack:", stack)

last_item = stack.pop()  # pop
print("Popped item:", last_item)
print("Stack after pop:", stack)

# ============================= Heap (data structure) =============================
# Heap: Tree-like structure, commonly used for priority queues
# directly access is not allowed

heap = []
heapq.heappush(heap, 30)
heapq.heappush(heap, 10)
heapq.heappush(heap, 20)
print("Heap (min-heap):", heap)

smallest = heapq.heappop(heap)
print("Smallest item popped:", smallest)
print("Heap after pop:", heap)

# ============================= Memory =============================
# Memory: Physical storage like RAM, SSD, Hard Disk
# Python manages memory automatically

# ============================= Garbage Collection =============================
# Garbage Collection: Automatically frees memory that is no longer used

class MyClass:
    def __init__(self, name):
        self.name = name
    def __del__(self):
        print(f"{self.name} is being deleted")

obj1 = MyClass("Object1")
del obj1  # object is eligible for garbage collection
gc.collect()  # force garbage collection

# ============================= Memory Management =============================
# Python automatically manages memory (allocation & deallocation)
# Ensures efficient use and avoids most memory leaks

# ============================= Memory Leak =============================
# Memory leak: Memory is still referenced even when not needed
leaky_list = []

def create_leak():
    for i in range(10000):
        leaky_list.append("x" * 1000)  # objects remain in memory

create_leak()
print("Memory leak simulated (objects still in memory)")
