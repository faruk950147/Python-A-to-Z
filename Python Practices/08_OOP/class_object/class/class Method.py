class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance methods (require object) that means instance method need object
    def showName(self):
        print(f"Name: {self.name}")

    def showAge(self):
        print(f"Age: {self.age}")

    def showInfo(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        
    # Class method (does not require object) that means class method does not need object
    @classmethod
    def showClassName(cls):
        print("Human")

    # Static method (does not require object or class reference) that means static method does not need object or class reference
    @staticmethod
    def showClassInfo():
        print("Human class")
        

if __name__ == "__main__":
    # Instance method examples
    human = Human("Faruk", 22)
    human.showName()
    human.showAge()
    human.showInfo()

    # Class and static method examples (no object needed)
    Human.showClassName()
    Human.showClassInfo()
