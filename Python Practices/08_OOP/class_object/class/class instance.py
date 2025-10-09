class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # instance method
    def showName(self):
        print(f"Name: {self.name}")
    # instance method
    def showAge(self):
        print(f"Age: {self.age}")
    # instance method
    def showInfo(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")