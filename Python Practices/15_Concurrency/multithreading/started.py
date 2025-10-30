# start() # Start the thread
# join() # Wait for the thread to finish

import threading
import time

# def display(num):
#     for i in range(num):
#         print(f"Hello World {i}")
# t = threading.Thread(target=display, args=(10,))
# t.start()

# def display2(num):
#     for i in range(num):
#         print(f"Hello Python {i}")
# t2 = threading.Thread(target=display2, args=(10,))
# t2.start()
# t2.join()

# class Custom(threading.Thread):
#    def display(self, num):
#       for i in range(num):
#          print(f"Hello World {i}")

# custom = Custom()
# t3 = Custom(target=custom.display, args=(10,))
# t3.start()
# t3.join()


class Custom(threading.Thread):
    def __init__(self, *args):
        threading.Thread.__init__(self)
        self.args = args

    def run(self):
        for i in range(*self.args):
            print(f"Hello World {i}")

t3 = Custom(10)
t3.start()
t3.join()
