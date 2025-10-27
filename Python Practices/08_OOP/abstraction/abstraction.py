# ====================== What is Abstraction ======================

# Abstraction is the process of hiding the implementation details of a class and showing only the necessary details to the user. It is a way to reduce the complexity of a program and make it easier to understand and maintain.

# ====================== Built-in abstract base class ======================

# Abstract Class
from abc import ABC, abstractmethod

# ======================
# Abstract Base Class
# ======================
class Car(ABC):
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.speed = 0      # Current speed
        self.gear = 0       # Current gear
        self.is_started = False  # Engine state

    # Abstract methods
    @abstractmethod
    def engine_start(self):
        pass

    @abstractmethod
    def engine_stop(self):
        pass

    @abstractmethod
    def drive(self):
        pass

    @abstractmethod
    def change_gear(self, gear):
        pass

    @abstractmethod
    def accelerate(self):
        pass

    @abstractmethod
    def brake(self):
        pass

    # Concrete method
    def current_speed(self):
        return self.speed


# ======================
# Subclass implementing all abstract methods
# ======================
class Tesla(Car):
    def engine_start(self):
        if not self.is_started:
            self.is_started = True
            return f"{self.name} engine started!"
        else:
            return f"{self.name} engine is already running!"

    def engine_stop(self):
        if self.is_started:
            self.is_started = False
            self.speed = 0
            return f"{self.name} engine stopped!"
        else:
            return f"{self.name} engine is already stopped!"

    def drive(self):
        if self.is_started:
            return f"{self.name} is driving at speed {self.speed} km/h in gear {self.gear}"
        else:
            return f"{self.name} cannot drive, engine is off!"

    def change_gear(self, gear):
        if self.is_started:
            self.gear = gear
            return f"{self.name} changed gear to {gear}"
        else:
            return f"{self.name} cannot change gear, engine is off!"

    def accelerate(self):
        if self.is_started:
            self.speed += 10 * self.gear if self.gear > 0 else 5
            return f"{self.name} accelerated to {self.speed} km/h"
        else:
            return f"{self.name} cannot accelerate, engine is off!"

    def brake(self):
        if self.speed > 0:
            self.speed -= 10
            if self.speed < 0:
                self.speed = 0
            return f"{self.name} slowed down to {self.speed} km/h"
        else:
            return f"{self.name} is already stopped!"


# ======================
# Interactive Usage
# ======================
if __name__ == "__main__":
    my_car = Tesla("Tesla Model S", "Red")

    print(my_car.engine_start())
    print(my_car.change_gear(1))
    print(my_car.accelerate())
    print(my_car.accelerate())
    print(my_car.change_gear(2))
    print(my_car.accelerate())
    print(my_car.drive())
    print(my_car.brake())
    print(my_car.brake())
    print(my_car.engine_stop())
