# Method Overriding is a feature of object-oriented programming (OOP) 
# that allows a subclass (child class) to redefine a method of its parent class. 
# This lets the subclass provide its own behavior while keeping the method name and 
# parameters are the same as in the parent class

# Method Overriding Example

class Parent:
    def __init__(self, name):
        self.name = name

    def show(self):
        print("Parent class show method:", self.name)

class Child(Parent):
    def __init__(self, name):
        super(Child, self).__init__(name)
    # Inherits __init__ from Parent, no need to redefine if same
    def show(self):  # Method overriding
        print("Child class show method:", self.name)
        # Optional: call parent method
        # super().show()

if __name__ == "__main__":
    c = Child("Child class")
    c.show()  # Output: Child class show method: Child class

