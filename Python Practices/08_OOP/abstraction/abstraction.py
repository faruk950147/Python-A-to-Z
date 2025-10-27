# # ====================== What is Abstraction ======================

# Abstraction is the process of hiding the implementation details of a class and showing only the necessary details to the user. It is a way to reduce the complexity of a program and make it easier to understand and maintain.

# ====================== Built-in abstract base class ======================

# Abstract Class
from abc import ABC, abstractmethod

class Car(ABC):
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.speed = 0
        self.acceleration = False
        self.braking = False
        self.engine_start = False
        self.engine_stop = False
        self.gear = 0
        
    @abstractmethod
    def start(self):
        self.engine_start = True
        return self.engine_start
    
    @abstractmethod
    def stop(self):
        self.engine_stop = True
        return self.engine_stop
    @abstractmethod
    def drive(self):
        return "Driving"
