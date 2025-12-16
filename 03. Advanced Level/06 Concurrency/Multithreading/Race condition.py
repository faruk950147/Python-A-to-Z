import threading
import time
# race condition is a situation where two or more threads access a shared resource and try to modify it at the same time.
# Shared resource (All buses are using this ticket counter)
available_seats = 5

class Bus(threading.Thread):
    def __init__(self, name, move_time):
        super().__init__()
        self.name = name
        self.move_time = move_time

    def run(self):
        global available_seats
        for i in range(3):  # each bus will try to book 3 seats
            print(f"{self.name} is checking seat availability...")
            time.sleep(self.move_time)

            if available_seats > 0:
                print(f"{self.name} found a seat! Booking now...")
                time.sleep(0.1)
                available_seats -= 1   # Shared resource change
                print(f"{self.name} booked a seat. Remaining seats: {available_seats}")
            else:
                print(f"{self.name} found no seat available!")
                
if __name__ == "__main__":
    bus1 = Bus("Bus-1", 0.2)
    bus2 = Bus("Bus-2", 0.2)
    bus3 = Bus("Bus-3", 0.2)

    bus1.start()
    bus2.start()
    bus3.start()

    bus1.join()
    bus2.join()
    bus3.join()

    print("All buses finished checking!")

balance = 100
class Account(threading.Thread):
    def withdraw(amount):
        global balance
        for _ in range(100000):
            balance -= amount

    def deposit(amount):
        global balance
        for _ in range(100000):
            balance += amount

    t1 = threading.Thread(target=withdraw, args=(1,))
    t2 = threading.Thread(target=deposit, args=(1,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

print("Final Balance:", balance)

""" 
class Account(threading.Thread):
    balance = 100  # Shared resource (All threads are using this balance)

    def __init__(self, name, amount, action):
        super().__init__()
        self.name = name
        self.amount = amount
        self.action = action  # 'deposit' or 'withdraw'

    def run(self):
        for _ in range(100000):
            if self.action == 'deposit':
                Account.balance += self.amount
            elif self.action == 'withdraw':
                Account.balance -= self.amount


t1 = Account("Thread-1", 1, 'withdraw')
t2 = Account("Thread-2", 1, 'deposit')

t1.start()
t2.start()

t1.join()
t2.join()

print("Final Balance:", Account.balance)


# race condition in python

 """