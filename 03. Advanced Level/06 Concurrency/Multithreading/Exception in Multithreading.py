# Exception in Multithreading is a type of exception that occurs when a thread encounters an error while executing a task.
import threading
import time

def display_numbers():
    for i in range(1, 11):
        print(i)
        time.sleep(1)

def display_letters():
    for letter in 'abcdefghij':
        print(letter)
        time.sleep(1)

thread1 = threading.Thread(target=display_numbers)
thread2 = threading.Thread(target=display_letters)

thread1.start()
thread2.start()

thread1.join()
thread2.join()