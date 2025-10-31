import threading
import time
# race condition is a situation where two or more threads access a shared resource and try to modify it at the same time.
# Shared resource (All buses are using this ticket counter)
available_seats = 5
# race condition
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

# Shared resource
available_seats = 5

# Lock for avoiding race condition
lock = threading.Lock()

class Bus2(threading.Thread):
    def __init__(self, name, move_time, lock):
        super().__init__()
        self.name = name
        self.move_time = move_time
        self.lock = lock

    def run(self):
        global available_seats
        for i in range(3):  # each bus will try to book 3 seats
            print(f"{self.name} is checking seat availability...")
            time.sleep(self.move_time)

            # Protect shared resource using lock
            with self.lock:
                if available_seats > 0:
                    print(f"{self.name} found a seat! Booking now...")
                    time.sleep(0.1)
                    available_seats -= 1   # Shared resource change
                    print(f"{self.name} booked a seat. Remaining seats: {available_seats}")
                else:
                    print(f"{self.name} found no seat available!")

# Create bus threads
bus1 = Bus2("Bus-A", 0.2, lock)
bus2 = Bus2("Bus-B", 0.3, lock)
bus3 = Bus2("Bus-C", 0.1, lock)

# Start all buses
bus1.start()
bus2.start()
bus3.start()

# Wait for all to finish
bus1.join()
bus2.join()
bus3.join()

print("\nFinal available seats:", available_seats)
