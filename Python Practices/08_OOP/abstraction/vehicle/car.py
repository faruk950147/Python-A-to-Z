# ====================== Abstraction using ======================
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.engine_started = False
        self.gear = 0

    # this method only shows how to start the car
    def start(self):
        self.engine_started = True
        print(f"{self.make} {self.model} is starting...")

    # this method only shows how to stop the car
    def stop(self):
        self.engine_started = False
        print(f"{self.make} {self.model} is stopping...")

    # this method only shows how to change gears
    def change_gear(self, gear):
        self.gear = gear
        print(f"{self.make} {self.model} is in gear {self.gear}")

# ====================== Usage ======================
car1 = Car("Toyota", "Corolla", 2022)
car1.start()
car1.stop()
car1.change_gear(1)