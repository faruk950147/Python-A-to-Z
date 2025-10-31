
import threading
import time
import os

event = threading.Event()

def clear_console():
    # Clear console (Windows / Linux)
    os.system('cls' if os.name == 'nt' else 'clear')

def light_switch(event):
    while True:
        # GREEN Light
        clear_console()
        print("""
        Traffic Light
        ----------------
        Red Light OFF
        Yellow Light OFF
        Green Light ON
        """)
        event.set()  # Allow crossing
        time.sleep(5)

        # YELLOW Light
        clear_console()
        print("""
        Traffic Light
        ----------------
        Red Light OFF
        Yellow Light ON
        Green Light OFF
        """)
        time.sleep(2)

        # RED Light
        clear_console()
        print("""
        Traffic Light
        ----------------
        Red Light ON
        Yellow Light OFF
        Green Light OFF
        """)
        event.clear()  # Stop crossing
        time.sleep(5)


def traffic_message(event):
    while True:
        if event.is_set():
            print("You can cross the road")
        else:
            print("You cannot cross the road")
        time.sleep(1)


if __name__ == "__main__":
    t1 = threading.Thread(target=light_switch, args=(event,))
    t2 = threading.Thread(target=traffic_message, args=(event,), daemon=True)

    t1.start()
    t2.start()

    t1.join()
