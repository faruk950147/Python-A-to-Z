# Abstract Class
from abc import ABC, abstractmethod

class Car(ABC):
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass
    def drive(self):
        print("Driving")

class Toyota(Car):
    def start(self):
        print("Toyota is starting")
    def stop(self):
        print("Toyota is stopping")
if __name__ == "__main__":
    toyota = Toyota()
    toyota.start()
    toyota.stop()
    toyota.drive()
