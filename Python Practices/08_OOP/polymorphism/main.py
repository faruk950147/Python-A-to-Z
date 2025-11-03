# polymorphism is a core concept in object-oriented programming (OOP) that allows objects of different classes to be treated as objects of a common superclass. It enables a single interface to represent different underlying forms (data types). 

class Animal:
    def speak(self):
        return "Some generic sound"
    
class Dog(Animal):
    def speak(self):
        return "Woof!"
    
class Cat(Animal):
    def speak(self):
        return "Meow!"
if __name__ == "__main__":
    animal = Animal()
    dog = Dog()
    cat = Cat()
    
    print(animal.speak())
    print(dog.speak())
    print(cat.speak())