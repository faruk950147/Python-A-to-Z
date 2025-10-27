class Human:
    # Class variable (shared by all instances)
    # This variable is common for all objects of the class
    species = "Homo sapiens"

    def __init__(self, name, age):
        # Instance variables (unique for each object)
        # Each object gets its own copy of these variables
        self.name = name
        self.age = age

    # Instance Methods
    # Require an object to call (use 'self' reference)
    # 'self' refers to the specific instance of the class
    def showName(self):
        print(f"Name: {self.name}")

    def showAge(self):
        print(f"Age: {self.age}")

    def showInfo(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

    # Class Method
    # Works with the class itself, not with instances
    # Takes 'cls' (class reference) instead of 'self'
    # Can access and modify class variables
    @classmethod
    def showClassName(cls):
        print(f"Class Name: {cls.__name__}")
        print(f"Species: {cls.species}")

    # Static Method
    # Does not take 'self' or 'cls'
    # Used for general-purpose utility functions
    # Logically included to the class but does not depend on class or instance data
    @staticmethod
    def showClassInfo():
        print("This is the Human class, representing all human beings.")


# Main Execution Block
if __name__ == "__main__":
    # Creating an object (instance)
    human = Human("Faruk", 22)

    # Instance method (object required)
    print("Instance Method Outputs:")
    human.showName()
    human.showAge()
    human.showInfo()

    print("------------------------")

    # Class method (no object required)
    print("Class Method Output:")
    Human.showClassName()

    print("------------------------")

    # Static method (no object or class reference required)
    print("Static Method Output:")
    Human.showClassInfo()
