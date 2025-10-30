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
