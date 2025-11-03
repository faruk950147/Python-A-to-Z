# Method Overriding is a feature of object-oriented programming (OOP) 
# that allows a subclass (child class) to redefine a method of its parent class. 
# This lets the subclass provide its own behavior while keeping the method name and 
# parameters are the same as in the parent class

# Method Overriding Example

# Parent Class
class Parent:
    def __init__(self, name):
        self.name = name

    def show(self):
        print("Parent class show method:", self.name)


# Child Class Examples

# Example 1: Using super()
class ChildSuper(Parent):
    def __init__(self, name):
        super().__init__(name)  # Parent constructor call

    def show(self):
        print("ChildSuper class show method:", self.name)
        super().show()  # Optional: call parent method


# Example 2: Using Parent class name
class ChildParentCall(Parent):
    def __init__(self, name):
        Parent.__init__(self, name)  # Directly call parent constructor

    def show(self):
        print("ChildParentCall class show method:", self.name)


# Example 3: Using self only
class ChildSelfOnly(Parent):
    def __init__(self, name):
        self.name = name  # Parent constructor skipped

    def show(self):
        print("ChildSelfOnly class show method:", self.name)


# Example 4: Parent call + extra attribute
class ChildExtra(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # Call parent constructor
        self.age = age  # Extra attribute optional but recommended

    def show(self):
        print(f"ChildExtra class: {self.name}, Age: {self.age}")
        super().show()


# Main Program
if __name__ == "__main__":
    c1 = ChildSuper("Alice")
    c1.show()
    print()

    c2 = ChildParentCall("Bob")
    c2.show()
    print()

    c3 = ChildSelfOnly("Charlie")
    c3.show()
    print()

    c4 = ChildExtra("Diana", 25)
    c4.show()
