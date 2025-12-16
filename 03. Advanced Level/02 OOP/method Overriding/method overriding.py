class Parent:
    def __init__(self, name):
        self.name = name

    def show(self):
        print("Parent class show method:", self.name)

class Child(Parent):
    def __init__(self, name):
        super().__init__(name)  # call Parent's constructor

    def show(self):  # Method overriding
        print("Child class show method:", self.name)
        super().show()  # optional: call parent's show method
if __name__ == "__main__":
    child = Child("FR")
    print(child.show()) 