# Static method is a method that is bound to the class and not the object of the class.
# It can't access or modify class state.
# It is marked with @staticmethod decorator.

# 1. change name of person class instance through object and can't change class variable name
# instance method
class Person:
    name = "John"

    def changeName(self, name):
        self.name = name   # here self means instance (object) it is new name created

if __name__ == "__main__":
    p1 = Person()
    p1.changeName("Doe")

    print(p1.name)       # Output: Doe
    print(Person.name)   # Output: John

# 2. change name of person class is can change class variable name through class
# class method
class Person2:
    name = "John"

    def changeName(self, name):
        Person2.name = name   # here class variable name is changed or modified it is changed name of class variable

if __name__ == "__main__":
    p1 = Person2()
    p1.changeName("Doe")

    print(p1.name)        # Output: Doe
    print(Person2.name)   # Output: Doe

# 3. static method
class Person3:
    name = "John"

    @staticmethod
    def changeName(name):
        Person3.name = name

if __name__ == "__main__":
    p1 = Person3()
    p1.changeName("Doe")

    print(p1.name)        # Output: Doe
    print(Person3.name)   # Output: Doe
