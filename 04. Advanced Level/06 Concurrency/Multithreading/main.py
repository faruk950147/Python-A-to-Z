import threading
import time

def first_program():
    for i in range(5):
        print("First Program:", i)
        time.sleep(1)

def second_program():
    for i in range(5):
        print("Second Program:", i)
        time.sleep(1)

# Thread তৈরি
t1 = threading.Thread(target=first_program)
t2 = threading.Thread(target=second_program)

# Thread start
t1.start()
t2.start()

# Main thread wait 
t1.join()
t2.join()

print("Program Finished")