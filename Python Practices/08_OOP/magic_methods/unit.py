# __init__
class Car:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def __str__(self):
        return f"{self.name} is {self.color}"
if __name__ == "__main__":
    car = Car("Toyota", "red")
    print(car)