# polymorphism is a core concept in object-oriented programming (OOP) 
# polymorphism means allows different classes to use the same method name +
# with different behaviors

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