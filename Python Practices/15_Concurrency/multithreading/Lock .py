# ===============================
# Lock Example in Python Threading
# ===============================
# Lock is a synchronization primitive that can be used to protect shared resources from concurrent access.
# It helps avoid race conditions.
# with lock: is a context manager that automatically acquires and releases the lock.
# acquire() is a blocking call. It will block the thread until the lock is available.
# that means if the lock is already held by another thread, the current thread will wait until the lock is released.
# release() is a non-blocking call. It releases the lock.
# that means it releases the lock and allows other threads to acquire it.
import threading

# ===============================
# 1st Method: Manual Lock Acquire/Release
# ===============================
balance = 100
lock = threading.Lock()

def withdraw(amount):
    global balance
    for _ in range(100000):
        lock.acquire()
        balance -= amount
        lock.release()

def deposit(amount):
    global balance
    for _ in range(100000):
        lock.acquire()
        balance += amount
        lock.release()

t1 = threading.Thread(target=withdraw, args=(1,))
t2 = threading.Thread(target=deposit, args=(1,))
t1.start()
t2.start()
t1.join()
t2.join()

print("1 Final Balance (Method 1):", balance)


# ===============================
# 2nd Method: Using 'with lock'
# ===============================
balance = 100
lock = threading.Lock()

def withdraw(amount):
    global balance
    for _ in range(100000):
        with lock:   # Automatically acquires and releases
            balance -= amount

def deposit(amount):
    global balance
    for _ in range(100000):
        with lock:
            balance += amount

t1 = threading.Thread(target=withdraw, args=(1,))
t2 = threading.Thread(target=deposit, args=(1,))
t1.start()
t2.start()
t1.join()
t2.join()

print("2 Final Balance (Method 2):", balance)


# ===============================
# 3rd Method: Lock inside Class (Object-level Lock)
# ===============================
class Account:
    def __init__(self, balance):
        self._balance = balance
        self.lock = threading.Lock()

    def withdraw(self, amount):
        with self.lock:
            self._balance -= amount

    def deposit(self, amount):
        with self.lock:
            self._balance += amount

    def transfer(self, amount, other_account):
        first, second = (self, other_account) if id(self) < id(other_account) else (other_account, self)
        with first.lock:
            with second.lock:
                if self._balance >= amount:
                    self._balance -= amount
                    other_account._balance += amount
                else:
                    print("Insufficient balance for transfer")

    def get_balance(self):
        return self._balance


if __name__ == "__main__":
    account1 = Account(100)
    account2 = Account(200)

    t1 = threading.Thread(target=account1.transfer, args=(100, account2))
    t2 = threading.Thread(target=account2.transfer, args=(100, account1))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print("3 Account 1 balance:", account1.get_balance())
    print("3 Account 2 balance:", account2.get_balance())


# ===============================
# 4th Method: Using @property and Lock
# ===============================
class Account:
    def __init__(self, balance):
        self._balance = balance
        self.lock = threading.Lock()

    @property
    def balance(self):
        """Getter for balance"""
        return self._balance

    @balance.setter
    def balance(self, value):
        """Setter for balance"""
        self._balance = value

    def withdraw(self, amount):
        with self.lock:
            self._balance -= amount

    def deposit(self, amount):
        with self.lock:
            self._balance += amount

    def transfer(self, amount, other_account):
        first, second = (self, other_account) if id(self) < id(other_account) else (other_account, self)
        with first.lock:
            with second.lock:
                if self._balance >= amount:
                    self._balance -= amount
                    other_account._balance += amount
                else:
                    print("Insufficient balance for transfer")


if __name__ == "__main__":
    account1 = Account(100)
    account2 = Account(200)

    t1 = threading.Thread(target=account1.transfer, args=(100, account2))
    t2 = threading.Thread(target=account2.transfer, args=(100, account1))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print("4 Account 1 balance:", account1.balance)
    print("4 Account 2 balance:", account2.balance)
